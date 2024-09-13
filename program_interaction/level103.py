#python
#!/usr/bin/python3.8
import subprocess
import os

fifo_path = 'test1'

if not os.path.exists(fifo_path):
    os.mkfifo(fifo_path)          //检测是否具有test1这个fifo

# 运行 /tmp/zkmdlw 程序
subprocess.run(['/challenge/run'] , stdin=open(fifo_path))

#terminal:
echo 'acdibxep' > test1 | python3.8 intera_script.py
