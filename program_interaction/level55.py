#!/usr/bin/python
import subprocess
p1 = subprocess.Popen(["/challenge/run"], stdout=subprocess.PIPE)#只能用Popen，其他会失败
p2 = subprocess.Popen(["grep", "pwn"], stdin=p1.stdout, stdout=subprocess.PIPE)
output = p2.communicate()[0]
print(output)
