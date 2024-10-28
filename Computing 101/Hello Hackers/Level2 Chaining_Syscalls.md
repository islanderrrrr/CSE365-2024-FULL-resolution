# 我来挑战简介
上一题其实我们写的是一个**write**程序，所以自然，我们还要有干净的退出程序

# 思路:
write一样，但是write结束并不代表整个程序的结束，我们要有个结束程序  
```
mov rax, 1
mov rdx, 1
mov rsi, 1337000
mov rdi, 1
syscall

mov rax, 60
mov rdi, 42
syscall
```
