# 挑战简介
是时候升级到 cIMG 的新版本了，这将更接近取代乏味的旧网络图像格式。找出不同之处，了解 /challenge/cimg 想要什么，然后获取标志！

# 思路
这个挑战要求你写一个最基础格式的cIMG文件，具体的要求在IDA中有表示出来

要求如下图  
<img width="771" alt="微信图片_20241129165429" src="https://github.com/user-attachments/assets/7b6088a1-a4fb-4ac0-b92d-2ad39d8163c5">  

<img width="635" alt="微信图片_20241129165457" src="https://github.com/user-attachments/assets/7c278e65-4597-4633-82f4-ed5726f66c72">  

可以看到，在最基础的前八字节格式后，后文数据的大小是要求1920字节的，而每一字节，分为4个字符数据，也就是8bit，分别为  
- 8C
- 1D
- 40 '@'
- 非空格字符 如'A'

**重复1920次即可**
```
#!/usr/bin/python

import struct

with open("test.cimg", "wb") as f:
    f.write(b'\x63\x49\x4D\x47')

    f.write(struct.pack("<H", 0x02))

    dimensions = 0x1850
    f.write(struct.pack("<H", dimensions))

    image_data = bytearray()
    for i in range(1920): 
        image_data.extend([0x8C, 0x1D, 0x40, 0x41]) 

    f.write(image_data)

```
