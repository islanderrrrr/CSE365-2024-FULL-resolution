#!/usr/bin/python3.8
import subprocess
import os
import sys

# 设置args[333]为nqhergldgq

args = ['']*332 +['nqhergldgq'];

# 清空环境变量，除了 LC_CTYPE
os.environ.clear()
os.environ["LC_CTYPE"] = os.getenv("LC_CTYPE", "")

# 设置挑战所需的环境变量
os.environ["22"] = "dnvedcjrnh"

# 执行挑战程序 /challenge/run并加入参数
subprocess.run(['/challenge/run'] + args, check=True)
