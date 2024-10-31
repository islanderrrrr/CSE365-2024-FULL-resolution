# 挑战简介
在这一关中，你将进行寄存器的操作。你需要修改或读取寄存器。

我们将在每次运行之前动态设置一些内存值，每次运行时这些值都会变化。这意味着你需要对寄存器进行某种公式计算。我们会告诉你哪些寄存器被设置，以及结果应该放在哪里。在大多数情况下，它是 rax。

使用你新学到的知识，请计算以下公式：
f(x)=mx+b，其中：
- m = rdi
- x = rsi
- b = rdx  
将结果放入 rax 中。

注意：mul（无符号乘法）和 imul（有符号乘法）在使用的寄存器上有重要区别。查看这些指令的文档以了解差异。

在这种情况下，你需要使用 imul。

# 思路
**简单的结合运算，利用好机制即可，宝宝巴士难度**
```
section .text
    global _start

_start:
    imul rdi, rsi
    add rdi, rdx
    mov rax, rdi 
```