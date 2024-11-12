# 挑战简介
===== 欢迎来到“构建 Web 服务器”！ =====
在此系列挑战中，您将编写程序集来与您的环境进行交互，并最终构建 Web 服务器
在此挑战中，您将把地址绑定到套接字。

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
我们先来了解bind的作用是什么  
**bind 是在服务器端编程中必要的一个步骤，尤其是在 TCP 服务器编程中。它的作用是明确告诉操作系统：哪个端口、哪个 IP 地址上的数据包应该与该套接字关联。**  
具体功能如下: 
1.  **设置网络接口（IP 地址）:** 指定套接字可以监听的本地 IP 地址。常见的地址设置包括：
  - 0.0.0.0（即 INADDR_ANY）：表示绑定到所有可用的网络接口，这样无论客户端连接哪个本地 IP 地址，都可以访问该端口。
  - 特定 IP 地址：可以绑定到本地机器的特定 IP 地址（如 127.0.0.1），表示仅允许通过该 IP 地址的连接。
2. **设置端口号：** 指定一个本地端口号，使服务能够监听该端口。当客户端发起请求时，可以通过这个端口和服务器通信。常用的端口包括：
  - 80：HTTP 协议的默认端口
  - 443：HTTPS 协议的默认端口

因此，bind作为在socket建立之后的一个步骤，起着与系统确立外部连接ip，port的重要方式

代码如下:
```
.intel_syntax noprefix
.globl _start

.section .text

_start:
    mov rax, 41       ; 系统调用号 41 对应 socket
    mov rdi, 2        ; domain = AF_INET (IPv4)
    mov rsi, 1        ; type = SOCK_STREAM (TCP)
    mov rdx, 0        ; protocol = IPPROTO_IP (默认协议)
    syscall            ; 执行系统调用
    mov r12, rax        ; 保存套接字文件描述符

    sub rsp, 16        ; 为 sockaddr_in 分配 16 字节空间
    
    mov word ptr [rsp], 2        ; sa_family (AF_INET)
    mov word ptr [rsp+2], 0x5000        ; 端口号 80，网络字节序（0x5000 -> htons(80)）
    mov word ptr [rsp+4], 0         ; IP 地址 (INADDR_ANY，即 0.0.0.0)

    mov rdi, r12                ; 套接字文件描述符
    mov rsi, rsp        ; sockaddr_in 结构体的地址
    mov rdx, 16        ; sockaddr_in 结构体的大小
    mov rax, 49        ; 系统调用号 49 对应 bind
    syscall        ; 执行系统调用

    add rsp, 16                    ; 清理栈上分配的空间

    mov rdi, 0
    mov rax, 60
    syscall

.section .data
```
