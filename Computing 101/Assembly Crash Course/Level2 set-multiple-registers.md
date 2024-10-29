# 挑战简介(我就是)
设置3个寄存器并赋值 没了

# 思路
**具体ELF可执行文件的操作见Level1**  

**这里展示汇编文件**
```
section .text
    global _start

_start:
    mov rax, 0x1337
    mov r12, 0xCAFED00D1337BEEF
    mov rsp, 0x31337
```
