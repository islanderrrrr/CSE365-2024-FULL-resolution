# 挑战简介
现在我们来谈谈对 cIMG 的高级设计所做的最后更改。文件格式往往会为解析程序提供许多指令来执行不同的操作。
例如，在 HTML 文件中，每个标签都是一个指令，可促使渲染引擎采取行动。图像文件也类似。我们将通过使用类似的概念扩展 cIMG 来开始探索格式和解析器之间的关系。

# 思路
**炼狱题**  
这一题我写了非常非常久，原因有几点，其一是不理解题意，其二便是硬实力的不足，what is directives?

不断地试，一直的试，结果却莫名其妙的出来了...挺无语的

我解释不了，就发个答案吧，求大佬解释

```
#!/usr/bin/python

import struct

def read_cleaned_info(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # 解析每一行
    cleaned_data = []
    for line in lines:
        # 去除可能的换行符和空格
        line = line.strip()
        # 分割每一行，假设每行是以逗号分隔的：R,G,B,Char
        parts = line.split(',')
        if len(parts) == 4:
            try:
                r, g, b, char = int(parts[0]), int(parts[1]), int(parts[2]), parts[3]
                if not char:  # 如果字符部分为空，跳过这一行或为其指定默认值
                    char = ' '  # 可以选择一个默认字符，如空格
                cleaned_data.append((r, g, b, char))
            except ValueError:
                print(f"Skipping invalid line: {line}")
        else:
            print(f"Skipping invalid line: {line}")
    
    return cleaned_data


# 将 RGB 和字符转换为十六进制数据
def convert_to_hex(cleaned_data):
    hex_data = b''  # 存储转换后的十六进制数据
    
    for r, g, b, char in cleaned_data:
        # 将 RGB 转换为字节
        hex_data += struct.pack('BBB', r, g, b)  # RGB (每个数为一个字节)
        # 将字符转换为字节（ASCII 转换）
        hex_data += struct.pack('B', ord(char))  # 字符转为字节
    
    return hex_data

# 将数据写入 test.cimg 文件
def write_cimg_file(hex_data, output_file="test.cimg"):
    with open(output_file, "wb") as f:
        # 写入固定头部数据
        f.write(b'\x63\x49\x4D\x47')  # 代表 cIMG
        
        # 写入 0x02 字节
        f.write(struct.pack("<H", 0x03))  # 写入一个无符号短整数 0x03
        
        # 假设的 dimensions
        dimensions = 0x184C
        f.write(struct.pack("<H", dimensions))  # 写入一个无符号短整数 0x184C

        f.write(b'\x01\x00\x00\x00')
        f.write(b'\x01\x00')

        
        # 写入从 cleaned_info.txt 转换来的十六进制数据
        f.write(hex_data)  # 直接写入十六进制数据

def main():
    # 假设 cleaned_info.txt 文件在当前目录
    cleaned_info_file = "cleaned_info.txt"
    
    # 读取文件并转换为十六进制数据
    cleaned_data = read_cleaned_info(cleaned_info_file)
    
    # 转换为十六进制字节数据
    hex_data = convert_to_hex(cleaned_data)
    
    # 将数据写入 .cimg 文件
    write_cimg_file(hex_data)
    
    print("File 'test.cimg' has been written successfully.")

if __name__ == "__main__":
    main()
    
```

送给大家一句话，在我绝望之际，一个老外的发言:  
****
**as a university student i would hate pwn.college (not easy to copy/paste from other,its learning by doing).but as i hobby this is great.**
