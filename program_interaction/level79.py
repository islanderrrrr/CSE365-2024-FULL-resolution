#!/usr/bin/python3.8
import os
import subprocess
from multiprocessing import Process #导入语法，Process语法是关于创造子进程的重要语法

os.makedirs('/tmp/another_directory', exist_ok=True) #检查是否具有当前路径并创建

os.chdir('/tmp/another_directory') #设置当前路径

def son():
    subprocess.run(['/challenge/run'], cwd="/tmp/rfdtev") #定义子进程，运行/challenge/run，并设置cwd(当前路径)为指定路径，此时父级路径为/tmp/another_directory


if __name__ == '__main__':
    p1=Process(target=son)
    p1.start() #运行子进程
    p1.join() #检查子进程是否完成
