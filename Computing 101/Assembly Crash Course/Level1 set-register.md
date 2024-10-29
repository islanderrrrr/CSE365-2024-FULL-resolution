# 挑战简介
In this level, you will be working with registers. You will be asked to modify or read from registers.

In this level, you will work with registers! Please set the following:

rdi = 0x1337

**简而言之，用寄存器工作，设置地址**

# 思路
**ELF文件是什么?**  
  我的理解:位于x86上的可执行目标文件

**关于ELF文件的转换**
1. 首先创建汇编文件
```
section .text
    global _start

_start:
    mov rdi, 0x1337  ; 设置 rdi 为 0x1337
    ; 在这里可以添加退出代码，防止程序崩溃
    mov rax, 60      ; 系统调用编号 60 (exit)
    syscall           ; 调用 exit
```
2. 使用汇编器将其汇编成 ELF 文件。你可以使用 nasm 命令：
```
nasm -f elf64 your_first_program.s -o your_first_program.o
```
3. 然后链接生成可执行文件:
```
ld your_first_program.o -o your_first_program
```
4. 最后，运行生成的 ELF 文件：
```
/challenge/run ./your_first_program
```

**开了个好头，这下有得做了**
