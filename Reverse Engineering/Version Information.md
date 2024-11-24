# 挑战简介
```
解析不断发展的文件格式的程序必须能够分辨出它必须解析的格式的版本。这通常存储在魔法数字附近。弄清楚如何为这个 /challenge/cimg 提供正确的 cIMG 版本！

写入二进制数据：您会发现需要创建包含您无法在键盘上键入的字符的文件。您可以通过多种方式执行此操作，但其中一种方法是创建一个 Python 脚本来为您制作此文件：

首先，打开您要写入的文件。

with open("my-file", "wb") as out_file:
上面的“wb”告诉 Python 打开“my-file”文件以写入原始字节。一旦我们有了这个，我们就可以写入它。当然，您熟悉文件的典型写入方式：

with open("my-file", "wb") as out_file:
out_file.write(b"HELLO WORLD")
如您所见，您可以正常输入的字符可以直接放入 Python 字节串中发送到文件。其他字符呢？正如您之前在 Python 字节串中看到的，您可以使用 \x“转义序列”通过其原始字节值指定字符。例如，\x41 创建一个十六进制值为 0x41 的字节，即 ASCII A。首先，让我们使用它以不同的方式写入上述内容：

with open("my-file", "wb") as out_file:
out_file.write(b"HELLO \x57\x4f\x52\x4c\x44")
这也会将 HELLO WORLD 写入文件！ Python 在执行代码时创建字节串时会解析转义序列

您可以使用其他值来制作原本无法输入的字符。例如，我们在 HELLO WORLD 后插入一个空字节（值 0）：

with open("my-file", "wb") as out_file:
out_file.write(b"HELLO \x57\x4f\x52\x4c\x44\x00")
空字节用于许多二进制格式和协议，还有许多其他字节具有难以输入的值。对于一些常见的字节，您可以使用其他“转义序列”作为简写。以下是几个示例：

assert b"\0" == b"\x00" # 我们的空字节
assert b"\n" == b"\x0a" # 换行符
您还需要“转义”字符，例如，这些字符会干扰 Python 语法本身。例如，这将打印 HELLO "WORLD"!:

with open("my-file", "wb") as out_file:
out_file.write(b"HELLO \"WORLD\"!")
上面的双引号必须转义，这样 Python 才不会将它们解释为字节串的结尾！

写入整数值：当然，文件格式中的某些字节表示整数，通常以小端格式存储。写入这些将要求您将典型整数（例如 5）“打包”为其二进制表示（这取决于变量的大小。例如，32 位/4 字节 1 将是 b"\x05\x00\x00\x00）。

要在整数和原始字节之间进行转换，请查看 struct Python 包。

with open("my-file", "wb") as out_file:
# 这将整数 1337（十六进制为 0x539）打包成四个小端字节
out_file.write(struct.pack("<I", 1337))

# 上述内容等同于
out_file.write(b"\x39\x05\x00\x00")

# 这将整数 1337（十六进制为 0x539）打包成两个小端字节
out_file.write(struct.pack("<H", 1337))

# 上述内容相当于
out_file.write(b"\x39\x05")
如果您感兴趣，可以查看 struct 文档中的其他格式说明符。
```

# 思路:
在文件格式中，版本号用来标识该文件的格式版本。不同的版本可能会有不同的解析方式，因此程序需要检查文件的版本号以确定该如何解析。

只需加个版本号即可

```
#!/usr/bin/python

import struct

with open("test.cimg", "wb") as f:
    f.write(b'\x63\x49\x4D\x47')

    f.write(struct.pack("<H", 0x01))
```
