# 挑战简介
We will now set some values in memory dynamically before each run. On each run, the values will change. This means you will need to perform some type of formulaic operation with registers. We will tell you which registers are set beforehand and where you should put the result. In most cases, it's rax.

In this level, you will be working with control flow manipulation. This involves using instructions to both indirectly and directly control the special register rip, the instruction pointer. You will use instructions such as jmp, call, cmp, and their alternatives to implement the requested behavior.

Recall that for all jumps, there are three types:

Relative jumps  
Absolute jumps  
Indirect jumps  
In this level, we will ask you to do a relative jump. You will need to fill space in your code with something to make this relative jump possible. We suggest using the nop instruction. It's 1 byte long and very predictable.

In fact, the assembler that we're using has a handy .rept directive that you can use to repeat assembly instructions some number of times: GNU Assembler Manual

Useful instructions for this level:

jmp (reg1 | addr | offset)  
nop  
Hint: For the relative jump, look up how to use labels in x86.

Using the above knowledge, perform the following:

Make the first instruction in your code a jmp.  
Make that jmp a relative jump to 0x51 bytes from the current position.  
At the code location where the relative jump will redirect control flow, set rax to 0x1.

# 思路:
很抽象，思路很简单，解法很抽象

需要你从0x1开始，到0x51进行赋值

官方说了，可以用.rept进行重复赋值，用法如下
```
    .rept number
        nop
    .endr
```
但是此题每次编译都会报错  
**error: parser: instruction expected**  
实在不了解，既然重复不管用，那就只能人工重复了  
**注意**:汇编算数用的16进制，0x格式，所以51位实际上要81次nop
```
section .text
global _start

_start:
    jmp short next       ; 从当前位置跳转 51 字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop
    nop
    nop
    nop
    nop
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop
    nop
    nop
    nop
    nop
    nop
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop
    nop
    nop
    nop
    nop
    nop                  ; 填充字节
    nop                  ; 填充字节
    nop
    nop
    nop
next:
    mov rax, 0x1        ; 在跳转的目标位置，将 rax 设置为 1
```
