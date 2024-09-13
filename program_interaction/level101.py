# 修改args[0]的值 

#可以先用ln(link) -s 把/challenge/run与/tmp/连接起来
ln -s /challenge/run /tmp/zkmdlw
#设置路径
export PATH=/tmp:$PATH

#shell里面
#!/usr/bin/python3.8
import subprocess
import os

# 运行 /tmp/zkmdlw 程序
subprocess.run(['/tmp/zkmdlw'], check=True)
