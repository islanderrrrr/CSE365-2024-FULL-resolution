# 挑战简介
===== 欢迎来到“构建 Web 服务器”！ =====
在此系列挑战中，您将编写程序集来与您的环境进行交互，并最终构建一个 Web 服务器
在此挑战中，您将退出一个程序。

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
这一系列挑战教你如何构建web服务器，你照着它一步步做即可  
第一个挑战让你写退出程序(从开始到退出)
