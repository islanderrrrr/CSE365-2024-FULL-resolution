# 挑战简介
计算机验证魔法数字的最便捷方式是将其视为数字。这就是本挑战的 /challenge/cimg 所做的，向您展示这些事情在实践中通常是如何完成的。在这里，我们有一个与上一个挑战不同的魔法数字（否则就不需要反转二进制了！）
。反转二进制，记住字节序，并通过标志的魔法数字检查。

# 思路
一样的思路，四个字，只不过这次用了整条数据  
一样的，cmp在IDA找，会找到一个四个字组成的大数字  
换个方法写python即可
```
#!/usr/bin/python

magic_number = 0x6E6E6F43
with open("test.cimg", "wb") as f:
    f.write(magic_number.to_bytes(4, byteorder='little'))
```
