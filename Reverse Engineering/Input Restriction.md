# 挑战简介
某些程序对其输入施加了特定限制。继续积累 cIMG 格式的知识，但要注意 /challenge/cimg 对您在此级别必须发送的附加数据的限制。(sm翻译)


# 思路
我来翻译，简单来说，就是对此次数据(除了前8个字节头)进行了限制，你需要避开限制的数据，对后面1920的字节进行填充

填充数据随便填便是了

```
#!/usr/bin/python

import struct

with open("test.cimg", "wb") as f:
    f.write(b'\x63\x49\x4D\x47')

    f.write(struct.pack("<H", 0x01))

    dimensions = 0x1850
    f.write(struct.pack("<H", dimensions))

    f.write(b'\x30' * 1920)
``` 
