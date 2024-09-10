#!/usr/bin/python3.8
import subprocess
import sys

# 定义 argv[305] 的值为 "oxeglyyici"
args = [''] * 305 + ['oxeglyyici']  # 创建一个长度为 307 的列表 'oxeglyyici'

# 执行挑战程序 /challenge/run，并传递正确的参数
subprocess.run(['/challenge/run'] + args, check=True)
