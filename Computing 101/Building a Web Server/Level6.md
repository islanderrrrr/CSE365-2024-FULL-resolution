# 挑战简介
===== 欢迎来到构建 Web 服务器！ =====
在此系列挑战中，您将编写程序集以与您的环境进行交互，并最终构建 Web 服务器
在此挑战中，您将响应 http 请求。

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
响应HTTP请求，最基本的返回则是 **"HTTP/1.0 200 OK\r\n\r\n"**  
我么要做的，则是写三个模块:
- 接收HTTP请求
- 响应HTTP请求
- 关闭客户端连接

代码如下
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

    mov rax, 50      ;50参数调用
    mov rdi, r12        ;r12套接字，赋值上第一个参数
    mov rsi, 0          ;backlog设置0
    syscall
   
    mov rdi, r12        ; socket 文件描述符
    mov rsi, 0        ; NULL
    mov rdx, 0        ; NULL
    mov rax, 43         ; syscall: accept
    syscall
    mov r13, rax            ; 保存客户端 socket 文件描述符

    sub rsp, 1024      ; 为读取请求创建一个 1024 字节的缓冲区
    mov rdi, r13        ; 客户端 socket 文件描述符
    mov rax, 0        ; syscall: read
    mov rsi, rsp      ; 使用栈作为缓冲区存储请求
    mov rdx, 1024      ; 读取最多 1024 字节
    syscall

    mov rdi, r13      ; 客户端 socket 文件描述符
    mov rax, 1        ; syscall: write
    lea rsi, [message]      ; 加载响应内容的地址
    mov rdx, 19      ; 响应内容长度,这里布置为何，无法获取message的len，只能手动定义
    syscall

    mov rax, 3        ; syscall: close
    mov rdi, r13      ; 关闭客户端 socket
    syscall

    mov rdi, 0
    mov rax, 60
    syscall

.section .data
message:
    .ascii "HTTP/1.0 200 OK\r\n\r\n"      ; .ascii才能正常解析语句
message_len = . - message        ; 不能用?
```
**说一下.ascii的作用**  
它会将 "string" 中的每个字符作为字节（ASCII 码值）放入当前的数据段中。需要注意的是，它不会自动添加字符串结尾的 null 字符（'\0'），所以如果你在操作这些字符串时需要 null 终结符（例如 C 字符串），你必须手动添加。
