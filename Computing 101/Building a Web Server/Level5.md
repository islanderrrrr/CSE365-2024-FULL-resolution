# 挑战简介
```
===== Welcome to Building a Web Server! =====
In this series of challenges, you will be writing assembly to interact with your environment, and ultimately build a web server
In this challenge you will accept a connection.

Usage: `/challenge/run <path_to_web_server>`

$ cat server.s
.intel_syntax noprefix
.globl _start

.section .text

_start:
    mov rdi, 0
    mov rax, 60     # SYS_exit
    syscall

.section .data

$ as -o server.o server.s && ld -o server server.o

$ strace ./server
execve("./server", ["./server"], 0x7ffccb8c6480 /* 17 vars */) = 0
exit(0)                                 = ?
+++ exited with 0 +++

$ /challenge/run ./server
```

# 思路
接收access请求，你需要一个access模块  
access组成以下几点:
- 系统调用编号是 43
- 套接文件描述符
- 客户端地址
- 地址长度

代码如下
```
.intel_syntax noprefix
.globl _start

.section .text

_start:
    mov rax, 41
    mov rdi, 2
    mov rsi, 1
    mov rdx, 0
    syscall
    mov r12, rax

    sub rsp, 16
    
    mov word ptr [rsp], 2
    mov word ptr [rsp+2], 0x5000
    mov word ptr [rsp+4], 0
    mov rdi, r12
    mov rsi, rsp
    mov rdx, 16
    mov rax, 49
    syscall

    add rsp, 16
    
    mov rax, 50
    mov rdi, r12
    mov rsi, 0
    syscall

    
    mov rdi, r12
    mov rsi, 0
    mov rdx, 0
    mov rax, 43 
    syscall
    mov r13, rax
_end:
    mov rdi, 0
    mov rax, 60
    syscall

.section .data
```

注意，执行尽量用/challenge/run path/to/server,不要用bash脚本执行，不要！
