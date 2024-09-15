import os
import subprocess
import threading

# FIFO 文件路径
fifo_out_path = 'output_fifo'

# 确保 FIFO 文件存在
if not os.path.exists(fifo_out_path):
    os.mkfifo(fifo_out_path)

# 从 FIFO 读取并输出内容
def read_from_fifo():
    with open(fifo_out_path, 'r') as fifo_out:
        while True:
            output = fifo_out.readline()
            if output:
                print(f"Output: {output.strip()}")
            else:
                break

# 启动读取线程
read_thread = threading.Thread(target=read_from_fifo)
read_thread.start()

# 启动 /challenge/run 并将 stdout 重定向到 FIFO
with open(fifo_out_path, 'w') as fifo_out:
    process = subprocess.Popen(['/challenge/run'], stdout=fifo_out)

# 等待进程结束
process.wait()

# 等待读取线程结束
read_thread.join()
