#!/usr/bin/python3.8
import subprocess
import os

# 确保 /tmp/tmpodf 目录存在
os.makedirs("/tmp/tmpodf", exist_ok=True)

# 设置当前工作路径 /tmp/tmpodf
os.chdir("/tmp/tmpodf")

# 确保 gvhrgy 文件存在
open("gvhrgy", "a").close()  # 如果文件不存在则创建

# 重定向输入文件
with open("gvhrgy", "r") as input_file:
    subprocess.run(['/challenge/run'], stdin=input_file)
