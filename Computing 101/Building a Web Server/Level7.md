# 挑战简介
```
==== 欢迎来到构建 Web 服务器！ =====
在此系列挑战中，您将编写程序集以与您的环境进行交互，并最终构建 Web 服务器
在此挑战中，您将响应对指定文件内容的 GET 请求。

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
对指定文件内容的访问，总共分为以下几个模块
- 提取文件路径，(根据请求头来提取)
- 打开请求文件
- 读取文件内容
- 发送文件内容
- 关闭文件连接

总体而言还是非常有难度的，包括提取指定路径，清空多余的http头内容等等。 
代码如下： 
```
```