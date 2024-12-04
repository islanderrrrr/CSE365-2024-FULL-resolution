# 挑战简介
程序会保留大量有关已采取或未来应采取的操作的内部状态。此版本的 /challenge/cimg 会跟踪比以前更多的状态，这使其能够在向您提供标记之前对您的输入施加严格要求。找出它想要的图像，然后得分！

方法建议：此挑战像以前一样处理和显示您的输入，并在此过程中保持要检查的预期状态。要了解您的输入应该是什么，您可以考虑以下典型的逆向工程管道方法：

了解程序期望其内部状态是什么以向您提供标记。您应该使用图形逆向工具（IDA 等）的组合来做到这一点，以形成关于程序对您的输入所做操作的假设，并使用运行时调试器（gdb）在运行时验证这些假设。
例如，在某些特定的汇编指令下，程序会决定是否向您提供标记。在您的图形逆向工具中找到这一点，然后在运行时使用 gdb 验证您的理解。努力理解它正在检查的数据的含义，至少在高层次上理解。
检查通常是在一些可疑数据（在本例中是图像的一些变换）和已知良好数据之间进行的。在这种情况下，后者是什么？
了解程序如何使用您的输入来生成它在决策过程中检查的“可疑”数据。程序实现算法，这些算法是可以理解的。将您的输入转换为程序用于决策的数据的算法是什么？您可以使用 gdb 验证这个假设吗？
您可以使用这些经过验证的知识来调整您的输入以稍微改变程序的行为（例如，在程序决定您没有得到标志之前再进一步）吗？
许多将数据从 A（在本例中是您的输入数据）转换为 B（在本例中是与已知良好数据进行比较的“可疑”数据）的算法可以反转以创建将 B 转换回 A 的算法。您可以使用从步骤 2 获得的知识来创建这样的算法吗？
换句话说，您能否创建一个算法，将程序的内部状态转换回输入数据？首先，手动将其应用于某些数据，看看它是否会对程序处理输入的方式产生影响。
现在，您有了一个算法，它可以获取程序的预期状态并生成输入数据，从而使程序达到该内部状态。接下来，您需要提取程序期望的“已知良好”内部状态。这可以通过多种方式完成，但两个首选是图形反转工具和调试器 (gdb)：
两者都可以完成将预期状态提取到文件的任务。
将步骤 3 中的算法应用于步骤 4 中提取的已知良好状态，以获得应触发预期状态的输入。将正确的元数据放在上面（程序需要的任何魔法数字等）并将其输入到程序中！

# 思路
**这题真的非常难，等于说前面学的只是只言片语，现在直接开大了···**  
首先说说思路吧:
- 最基础的格式需要固定住，比如魔术四位，版本两位，长宽两位(此题版本02,长宽4c,18)
- 你需要使用strings语法，分解/challenge/cimg的组成部分
- 对于分解后的文本，进行清理，清理出需要输入的数据，称为clean_info.txt
- 清理完毕后，需要开始对数据进行regex(正则表达式)，提取出里面的rgb颜色，字符(颜色3位，字符1位)
- 提取完毕，将其转变为十六进制数，再写入test.cimg包中，即可

检测hex数的状况，可以用hexdump -C 观察  
只能说，有趣就完事了

代码如下  
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
        f.write(struct.pack("<H", 0x02))  # 写入一个无符号短整数 0x02
        
        # 假设的 dimensions
        dimensions = 0x184C
        f.write(struct.pack("<H", dimensions))  # 写入一个无符号短整数 0x184C
        
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
