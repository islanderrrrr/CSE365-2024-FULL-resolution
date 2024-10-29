# 挑战简介

在这一关中，你将进行寄存器的操作。我们将动态设置一些内存值，每次运行时这些值会变化。这意味着你需要对寄存器进行公式计算。我们会告诉你哪些寄存器被设置，以及你应该将结果放在哪里。在大多数情况下，它是 rax。

许多指令允许你在寄存器和内存上执行常规数学运算。

简而言之，当我们说 A += B 时，实际上是指 A = A + B。

以下是一些有用的指令：

add reg1, reg2 <=> reg1 += reg2  
sub reg1, reg2 <=> reg1 -= reg2  
imul reg1, reg2 <=> reg1 *= reg2  
div 更复杂，我们稍后再讨论。注意：所有 regX 都可以用常量或内存位置替代。
请执行以下操作：

将 0x331337 加到 rdi。

# 思路
寄存器的加减乘除运算
- add 加法
- sub 减法
- imul 乘法
- div 除法
**以下是汇编文件的实现(不难)**  
```
section .text
    global _start

_start:
    add rdi, 0x331337
```