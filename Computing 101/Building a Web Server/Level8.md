# 挑战简介
```
===== 欢迎来到“构建 Web 服务器”！ =====
在此系列挑战中，您将编写程序集来与您的环境进行交互，并最终构建一个 Web 服务器
在此挑战中，您将接受多个请求。

用法：`/challenge/run <path_to_web_server>`

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
这题相比于上一题，区别在于，这一次需要多次的接收路径，也就是多次accept  
很容易想到，一个jmp可以解决   
```
.intel_syntax noprefix
.globl _start

.section .text

_socket:
    mov rax, 41       ; 系统调用号 41 对应 socket
    mov rdi, 2        ; domain = AF_INET (IPv4)
    mov rsi, 1        ; type = SOCK_STREAM (TCP)
    mov rdx, 0        ; protocol = IPPROTO_IP (默认协议)
    syscall            ; 执行系统调用
    mov r12, rax        ; 保存套接字文件描述符

_bind:
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

_listen: 
    mov rax, 50      ;50参数调用
    mov rdi, r12        ;r12套接字，赋值上第一个参数
    mov rsi, 0          ;backlog设置0
    syscall

_accept:    
    mov rdi, r12        ; socket 文件描述符
    mov rsi, 0        ; NULL
    mov rdx, 0        ; NULL
    mov rax, 43         ; syscall: accept
    syscall
    mov r13, rax            ; 保存客户端 socket 文件描述符

_read_request:
    sub rsp, 1024      ; 为读取请求创建一个 1024 字节的缓冲区
    mov rdi, r13        ; 客户端 socket 文件描述符
    mov rax, 0        ; syscall: read
    mov rsi, rsp      ; 使用栈作为缓冲区存储请求
    mov rdx, 1024      ; 读取最多 1024 字节
    syscall

    lea rdi, [rsp+4]        # rdi 指向文件路径的开始（去掉 "GET " 前缀）
    xor rdx, rdx        # 清空 rdx，准备用它作为计数器

extract_path:
    mov al, byte ptr [rdi+rdx]        # 读取请求中的下一个字节
    cmp al, ' '        # 如果遇到空格（路径的结束标志），就跳出
    je path_extracted        # 如果遇到空格，说明路径提取完毕
    inc rdx        # 否则，继续向后移动
    jmp extract_path

path_extracted:
    mov byte ptr [rdi+rdx], 0            # 在路径末尾加上空字符，作为字符串的终止符

_open_file:
    lea rdi, [rsp+4]            # 请求的路径
    mov rsi, 0            # O_RDONLY
    mov rax, 2            # SYS_open
    syscall
    mov r14, rax            # 保存文件描述符

_read_files:
    sub rsp, 1024            # 为文件内容分配缓冲区
    mov rdi, r14            # 文件描述符
    mov rsi, rsp            # 缓冲区存放文件内容
    mov rdx, 1024            # 最大读取字节数
    mov rax, 0            # SYS_read
    syscall
    mov r15, rax            # 保存实际读取的字节数

_close_read:
    mov rdi, r14             # 文件描述符
    mov rax, 3                # SYS_close
    syscall

_respond_http_message:
    mov rdi, r13      ; 客户端 socket 文件描述符
    mov rax, 1        ; syscall: write
    lea rsi, [message]      ; 加载响应内容的地址
    mov rdx, 19      ; 响应内容长度,这里布置为何，无法获取message的len，只能手动定义
    syscall

_write_operation:
    mov rdi, r13            # 连接文件描述符
    mov rsi, rsp            # 文件内容缓冲区
    mov rdx, r15            # 文件内容的字节数
    mov rax, 1            # SYS_write
    syscall

_close_http_request:
    mov rax, 3        ; syscall: close
    mov rdi, r13      ; 关闭客户端 socket
    syscall

_continue:
    jmp _accept        ; 跳转到_accept模块，继续循环即可

_exit:
    mov rdi, 0
    mov rax, 60
    syscall

.section .data
message:
    .ascii "HTTP/1.0 200 OK\r\n\r\n"      ; .ascii才能正常解析语句
message_len = . - message        ; 不能用?
```
