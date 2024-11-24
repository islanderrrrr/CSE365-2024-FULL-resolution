# 挑战简介
让我们继续构建 cIMG 格式。 图像需要什么？ 尺寸！ 在此处指定正确的 Flag，然后获取您的标志！

# 思路
简单阐述一下要求，给这个图片一个尺寸，以及1920的data数据(不理解)，即可

```
#!/usr/bin/python

import struct

with open("test.cimg", "wb") as f:
    f.write(b'\x63\x49\x4D\x47')

    f.write(struct.pack("<H", 0x01))

    dimensions = 0x1850
    f.write(struct.pack("<H", dimensions))

    f.write(b'\x00' * 1920)
```

为了更了解其结构，我们来个hexdump

```
hacker@reverse-engineering~metadata-and-data:~$ hexdump -C test.cimg
00000000  63 49 4d 47 01 00 50 18  00 00 00 00 00 00 00 00  |cIMG..P.........|
00000010  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000780  00 00 00 00 00 00 00                              |.......|
00000787
```
