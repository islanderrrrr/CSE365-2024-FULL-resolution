# 挑战简介
用c写一个带有cimg魔数的cimg文件

# 思路
值得注意的是，python与c语言所解析的魔数是不同的，所以你要写入cimg的文件内容也不同

```
#!/usr/bin/python
import struct

with open("solution.cimg", "wb") as f:
    # 写入魔数 {Onr
    f.write(b"{Onr")
```
