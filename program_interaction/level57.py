#!/usr/bin/python
import subprocess
p1 = subprocess.Popen(["/challenge/run"], stdout=subprocess.PIPE)#只能用Popen，其他会失败
p2 = subprocess.Popen(["rev"], stdin=p1.stdout, stdout=subprocess.PIPE)
output = p2.communicate()[0]
print(output)

#没啥说的，就是将/challenge/run 的执行结果，作为输入进rev指令
#rev注意反转问题，需要输入反转后的密码来转正
#python
