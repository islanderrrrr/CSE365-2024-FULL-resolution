#!/usr/bin/python3.8
import subprocess
import os

# 清空环境变量，除了 LC_CTYPE
os.environ.clear()
os.environ["LC_CTYPE"] = os.getenv("LC_CTYPE", "")

# 设置挑战所需的环境变量
os.environ["231"] = "pqoiuqzdkp"

# 执行挑战程序 /challenge/run
subprocess.run(['/challenge/run'], check=True)
