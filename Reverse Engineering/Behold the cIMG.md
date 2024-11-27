# 挑战简介
现在该看看您的第一个 cIMG 了！让程序显示具有正确属性的图像，它就会给您标志。


# 思路
去IDA解析一下原汇编代码，你会发现一个逻辑，第一次执行数据对比时，计数器设置了113h(就是275)

可知，你需要写275个不为空的不限制的数据，比如字母

275个字符检测完毕后，返回主函数，进行后续的数据对比

后续数据需要是20h，16进制也就是' '(空格)

这下就ez了

```
#!/usr/bin/python

import struct

with open("test.cimg", "wb") as f:
    f.write(b'\x63\x49\x4D\x47')

    f.write(struct.pack("<H", 0x01))

    dimensions = 0x1850
    f.write(struct.pack("<H", dimensions))

    image_data = bytearray(275)
    for i in range(275):
        image_data[i] = 0x41 

    f.write(image_data)    
    f.write(b' ' * 1920)
```
