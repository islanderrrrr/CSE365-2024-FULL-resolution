# 挑战简介
```
===== 欢迎来到“构建 Web 服务器”！ =====
在此系列挑战中，您将编写程序集来与您的环境进行交互，并最终构建一个 Web 服务器
在此挑战中，您将响应多个并发的 GET 和 POST 请求。

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
处理多个并发的GET和POST，只需要将Level8和Level10结合起来即可，不过要注意的就是要对两种请求进行分区，避免混淆

唯一的难点可能就是，多个POST请求，正文长度不一，要对无关字符进行跳过处理
还有就是GET和POST的结合处理

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

_fork:
    mov rax, 57      ; 系统调用号：fork
    syscall        ; 执行 fork 系统调用
    test rax, rax        ; 判断 fork 的返回值
    jz child_process       ; 如果返回值为 0，进入子进程
    jg parent_process        ; 如果返回值大于 0，继续执行父进程

child_process:
  ; 子进程：关闭监听套接字，处理请求
    mov rdi, r12        ; 关闭父进程的套接字描述符
    mov rax, 3          ; 系统调用号：close
    syscall

_read_request:
    sub rsp, 1024      ; 为读取请求创建一个 1024 字节的缓冲区
    mov rdi, r13        ; 客户端 socket 文件描述符
    mov rax, 0        ; syscall: read
    mov rsi, rsp      ; 使用栈作为缓冲区存储请求
    mov rdx, 1024      ; 读取最多 1024 字节
    syscall

    lea rsi, [rsp]      ; 此模块作用是判定POST或GET
    lea rdi, [str_post]      ; 设置rdi为POST字段
    mov rcx, 4          ; 判定区间4个字符

_compare_to_mthod:        
    lodsb              ; 从 rsi 指向的内存读取一个字节到 al，并让 rsi 自动递增，准备比较。
    scasb              ; 比较 al 中的当前字节值和 rdi 所指向位置的字节（参考字符串的当前字符）。
    jne _extract_GET   ; 不等则跳转
    loop _compare_to_mthod      ; 循环判定，每次rcx-1

_extract_POST:
    lea rdi, [rsp+5]         ; 越过"POST "到文件路径
    mov r11, 1                ; 作为POST的证明
    xor rdx, rdx            ; 清空rdx
    jmp extract_path_POST        ; 跳转到POST路径提取

_extract_GET:
    lea rdi, [rsp+4]           ; 到文件路径
    xor r11, r11                ; 使r11为0，作为证明
    xor rdx, rdx
    jmp extract_path_GET        ; 跳转GET路径提取

extract_path_POST:
    mov al, byte ptr [rdi+rdx]        ; 遇到空符号，则跳转
    cmp al, ' '
    je path_extracted        
    inc rdx                        ; 没遇到，则增加偏移量
    jmp extract_path_POST           ; 循环 

extract_path_GET:                    ; 同上 
    mov al, byte ptr [rdi+rdx]
    cmp al, ' '
    je path_extracted
    inc rdx
    jmp extract_path_GET

path_extracted:
    mov byte ptr [rdi+rdx], 0        ; 将结束符作为路径的结尾
    cmp r11, 0                        ; 判定，跳转GET的处理
    je _open_file_GET

_open_file_POST:
    lea rdi, [rsp+5]            # 请求的路径
    mov rsi, 65            # O_WRONLY|O_CREAT
    mov rdx, 511            # 加权0777是511
    mov rax, 2            # open文件
    syscall
    mov r14, rax            # 保存文件描述符

_defi_length:                # POST文件内容在本题中有十位长度或百位长度
    lea rsi, [rsp+182]        # 默认为十位长度
    xor rcx, rcx                # 清零计数器

extract_message:
    mov al, byte ptr [rsi + rcx]      # 赋值内容每一个字符
    cmp al, 0                      # 如果为0，则跳转写入
    je _write_files                
    cmp al, '\n'                    # 如果是换行符，跳过
    je skip_newline
    inc rcx                        # 递增计数器
    jmp extract_message            # 循环重复

skip_newline:
    lea rsi, [rsp+183]         # 则为百位长度
    xor rcx, rcx                
    jmp extract_message        # 再次开始提取内容

_write_files:
    mov rdi, r14            # 文件描述符
                            # rsi为内容，已储存
    mov rdx, rcx            # rcx内容长度
    mov rax, 1            # SYS_write
    syscall
    mov r15, rax            # 保存实际读取的字节数
    jmp _close_read

_open_file_GET:
    lea rdi, [rsp+4]        #  打开文件，获取文件地址
    mov rsi, 0            # O_RDONLY
    mov rax, 2              # SYS_open 
    syscall
    mov r14, rax            # 存储文件描述符 

_read_files:
    sub rsp, 1024            # 为文件内容分配缓冲区
    mov rdi, r14                # 文件描述符
    mov rsi, rsp            # 缓冲区存放文件内容
    mov rdx, 1024            # 最大读取字节数
    mov rax, 0                # SYS_read
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
    mov rdx, 19      ; 响应内容长度,这里不知为何，无法获取message的len，只能手动定义
    syscall
    cmp r11, 1
    je _exit

_write_operation_GET:
    mov rdi, r13            # 连接文件描述符
    mov rsi, rsp            # 文件内容缓冲区
    mov rdx, r15            # 文件内容的字节数
    mov rax, 1            # SYS_write
    syscall

_exit:
    mov rdi, 0
    mov rax, 60
    syscall

parent_process:
  ; 父进程：关闭客户端套接字

_close_parent:
    mov rdi, r13      ; 客户端套接字描述符
    mov rax, 3        ; 系统调用号：close
    syscall

_continue_accept:
    jmp _accept        ; accept循环

.section .data
message:
    .ascii "HTTP/1.0 200 OK\r\n\r\n"      ; .ascii才能正常解析语句
message_len = . - message        ; 不能用?

str_post: 
    .ascii "POST"
```

# 至此，一锤定音；尘埃，已然落定！
