# 挑战简介
此题储存了一个14字节长的字符串在[1337000]地址，把他输出出来吧！

# 思路:
rdx代表了所要输出的字符长度，修改为14即可
```
mov rax, 1
mov rdx, 14
mov rsi, 1337000
mov rdi, 1
syscall

mov rax, 60
mov rdi, 42
syscall
```
***
**完结撒花**
