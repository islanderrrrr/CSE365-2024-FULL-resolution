# 挑战简介
先sort排序

将index[6]与index[19]调换

异或，依旧是余三，分别异或0b d9 e0  

逆转

将index[4]与index[12]调换

# 思路
思路也就如上了，操作过程相当于加密解密，能AI跑的前提就是你要明白思路  

```
#!/usr/bin/python
from pwn import *
import struct
import os
cache_dir = '/tmp/.pwntools-cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

context(os='linux', arch='amd64', log_level='debug', cache_dir=cache_dir)
p = process('/challenge/babyrev-level-7-0')

payload=b'\x61\x63\x64\x66\x67\x6a\x6a\x6b\x6b\x6d\x6d\x6d\x6d\x6e\x6f\x70\x70\x70\x71\x72\x74\x75\x75\x78\x78'

p.recvuntil('Ready to receive your license key!\n')

p.send(payload)

output = p.recvall()
print(output.decode(errors='ignore'))

```
