# 挑战简介
在这一级别中，您将使用控制流操作。这涉及使用指令间接和直接控制特殊寄存器 rip，即指令指针。您将使用 jmp、call、cmp 等指令及其替代指令来实现所请求的行为。

我们将在这一级别使用动态值多次测试您的代码！这意味着我们将以各种随机方式运行您的代码，以验证逻辑是否足够强大，可以承受正常使用。

我们现在将向您介绍条件跳转 - x86 中最有价值的指令之一。在高级编程语言中，存在一个 if-else 结构来执行以下操作：

如果 x 为偶数：  
is_even = 1  
else：  
is_even = 0  
这应该看起来很熟悉，因为它只能在位逻辑中实现，您在上一级别中已经做过了。在这些结构中，我们可以根据提供给程序的动态值来控制程序的控制流。

使用 jmps 实现上述逻辑可以这样做：
```
;假设 rdi = x，rax 是输出  
; rdx = rdi mod 2  
mov rax, rdi  
mov rsi, 2  
div rsi  
; 如果余数为偶数，则余数为 0  
cmp rdx, 0  
; 如果不是 0，则跳转到 not_even 代码  
jne not_even  
; 转到偶数代码  
mov rbx, 1
jmp done
; 仅在 not_even 时跳转到此处
not_even:
mov rbx, 0
done:
mov rax, rbx
; 更多说明请见此处
不过，通常情况下，您需要的不仅仅是一个“if-else”。有时您需要两个 if 检查，然后是 else。为此，您需要确保您的控制流在失败后“跳转到”下一个 if。执行后，所有代码都必须跳转到相同的 done，以避免 else。
```

x86 中有许多跳转类型，了解它们的使用方法会有所帮助。几乎所有跳转类型都依赖于称为 ZF（零标志）的东西。当 cmp 相等时，ZF 设置为 1，否则设置为 0。

利用上述知识，实现以下内容：

如果 [x] 为 0x7f454c46：  
y = [x+4] + [x+8] + [x+12]  
否则，如果 [x] 为 0x00005A4D：  
y = [x+4] - [x+8] - [x+12]  
否则：  
y = [x+4] * [x+8] * [x+12]  
其中：  

x = rdi，y = rax。  
假设每个取消引用的值都是有符号的双字。这意味着值可以在每个内存位置以负值开始。

有效的解决方案将至少使用一次以下内容：

jmp（任何变体）、cmp

# 思路
此题便开始要求你用汇编来实现一些算法

这是一个典型的if-else算法

```
section .text
global _start

_start:
    mov eax, [rdi]         ; Load the value at x into rax
    cmp eax, 0x7f454c46    ; Compare with first value      ;cmp相等即位1，只懂这些了
    je  is_7f454c46        ; Jump if equal      ;je的意思，即符合就跳转
    cmp eax, 0x00005A4D    ; Compare with second value
    je  is_5A4D            ; Jump if equal
    jmp else_case          ; Otherwise, jump to else case

is_7f454c46:
    ; Load, add values, and store in rax
    mov eax, [rdi+4]
    add eax, [rdi+8]
    add eax, [rdi+12]
    jmp done

is_5A4D:
    ; Load, subtract values, and store in rax
    mov eax, [rdi+4]
    sub eax, [rdi+8]
    sub eax, [rdi+12]
    jmp done

else_case:
    ; Load, multiply values, and store in rax
    mov eax, [rdi+4]
    imul eax, [rdi+8]
    imul eax, [rdi+12]

done:
```
