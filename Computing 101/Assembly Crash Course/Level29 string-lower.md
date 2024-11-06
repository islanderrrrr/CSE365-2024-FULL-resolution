**诶呀，tm这道题写了快两天，真升华了**
# 挑战简介
在这一关中，我们将使用动态值多次测试您的代码！这意味着我们将以各种随机方式运行您的代码，以验证逻辑是否足够强大，可以承受正常使用。

在这一关中，您将使用函数！这将涉及操纵指令指针 (rip)，以及执行比平时更难的任务。您可能会被要求使用堆栈来存储值或调用我们提供给您的函数。

在之前的关卡中，您实现了一个 while 循环来计算连续内存区域中连续非零字节的数量。

在这一关中，您将再次获得一个连续的内存区域，并将循环执行每个条件操作，直到达到零字节。所有这些都将包含在一个函数中！

函数是一段可调用的代码，不会破坏控制流。

函数使用指令“call”和“ret”。

“call”指令将下一条指令的内存地址推送到堆栈上，然后跳转到存储在第一个参数中的值。

让我们使用以下指令作为示例：
```
0x1021 mov rax, 0x400000
0x1028 call rax
0x102a mov [rsi], rax
call 将下一条指令的地址 0x102a 推送到堆栈上。
call 跳转到 0x400000，即存储在 rax 中的值。
“ret”指令与“call”相反。
```
ret 从堆栈中弹出顶部值并跳转到该值。

让我们使用以下指令和堆栈作为示例：

堆栈地址值
```
0x103f mov rax, rdx RSP + 0x8 0xdeadbeef
0x1042 ret RSP + 0x0 0x0000102a
这里，ret 将跳转到 0x102a。
```
请实现以下逻辑：
```
str_lower(src_addr):
i = 0
if src_addr != 0:
while [src_addr] != 0x00:
if [src_addr] <= 0x5a:
[src_addr] = foo([src_addr])
i += 1
src_addr += 1
return i
```
foo 在 0x403000 处提供。foo 将单个参数作为值并返回一个值。

所有函数（foo 和 str_lower）都必须遵循 Linux amd64 调用约定（也称为 System V AMD64 ABI）：System V AMD64 ABI

因此，您的函数 str_lower 应该在 rdi 中查找 src_addr，并将函数返回放在 rax 中。

需要注意的是，src_addr 是内存中的地址（字符串所在的位置），而 [src_addr] 指的是 src_addr 中存在的字节。

因此，函数 foo 接受一个字节作为其第一个参数并返回一个字节。

# 思路:
**这思路我可得好生说了**  
这个逻辑简单来说:  
- 一个字符串，找出里面所有的大写字母，转写成小写字母
- 其中,rax为i，src_addr为rdi,src_addr存储的数据为[rdi]

这时候你会想怎么做?有几个毒点
- rax作为foo函数返回的存储值，rax的作用有重叠，需要另一个寄存器代替存储
- rdi作为传进去的参数，rdi本是地址，你传进去的需要是数值，所以你也需要另一个寄存器存储rdi每次循环的地址

**代码献上！**
```
section .text
    global _start
    extern foo

_start:
    xor rsi, rsi
    xor rax, rax
    mov rcx, 0x403000
    cmp rdi, 0
    jz set_zero

loop:
    mov dl, byte [rdi]
    test dl, dl 
    jz set_zero
    cmp dl, 0x5A
    jg skip_num

    mov rbx, rdi
    movzx rdi, dl
    call rcx    #这边foo函数的地址也要一个寄存器，否则会报错地址非法使用(why?)
    mov dl, al
    mov byte [rbx], dl
    mov rdi, rbx
    inc rsi

skip_num:
    add rdi, 1    转移到下一个字节
    jmp loop

set_zero:
    mov rax, rsi
    ret
```
