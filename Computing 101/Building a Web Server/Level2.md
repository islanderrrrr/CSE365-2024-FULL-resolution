# 挑战简介
===== 欢迎来到“构建 Web 服务器”！ =====
在此系列挑战中，您将编写程序集来与您的环境进行交互，并最终构建一个 Web 服务器
在此挑战中，您将创建一个套接字。

用法：`/challenge/run <path_to_web_server>`
```
$ cat server.s
.intel_syntax noprefix
.globl _start

.section .text

_start:
mov rdi, 0
mov rax, 60 # SYS_exit
syscall

.section .data

$ as -o server.o server.s && ld -o server server.o

$ strace ./server
execve("./server", ["./server"], 0x7ffccb8c6480 /* 17 vars */) = 0
exit(0) = ?
+++ 退出，结果为 0 +++

$ /challenge/run ./server
```

# 思路
创建一个socket  
socket是有调用编码的，一般调用编码用rax来传递，socket的调用编码是41  
对于参数的传递，寄存器也有一套顺序:  
1. 第 1 个参数：rdi
2. 第 2 个参数：rsi
3. 第 3 个参数：rdx
4. 第 4 个参数：r10
5. 第 5 个参数：r8
6. 第 6 个参数：r9
根据函数**socket(AF_INET, SOCK_STREAM, IPPROTO_IP) = 3**我们知道，我们要传递的参数有3个，也就是顺序的前三个  
代码如下:
```
.intel_syntax noprefix
.globl _start

.section .text

_start:
    mov rax, 41
    mov rdi, 2      ; domain = 2 (AF_INET6, IPv6)
    mov rsi, 1      ; type = 1 (SOCK_STREAM, TCP)
    mov rdx, 0      ; protocol = 0 (IPPROTO_IP, 默认协议)
    syscall

    mov rdi, 0
    mov rax, 60
    syscall

.section .data
```
