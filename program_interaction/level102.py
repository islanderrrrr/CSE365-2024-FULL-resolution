#args[0]从路径改成了参数，PATH要变
ln -s /challenge/run cxvwut
export PATH=.:$PATH

python:
#!/usr/bin/python3.8
import subprocess
import os


# 运行 /tmp/zkmdlw 程序
subprocess.run(['cxvwut'] , check=True)
