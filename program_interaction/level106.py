import os
import subprocess
import threading

# FIFO 文件路径
fifo_in_path = 'input_fifo'
fifo_out_path = 'output_fifo'

# 向 FIFO 写入用户输入的答案
def write_to_fifo():
    with open(fifo_in_path, 'w') as fifo_in:
        # 从用户获取输入并写入 FIFO
        while True:
            user_input = input("Enter your answer: ")
            fifo_in.write(user_input + '\n')
            fifo_in.flush()

# 从 FIFO 读取并显示输出
def read_from_fifo():
    with open(fifo_out_path, 'r') as fifo_out:
        while True:
            output = fifo_out.readline()
            if output:
                print(f"Output: {output.strip()}")
            else:
                break

# 创建 FIFO 文件
if not os.path.exists(fifo_in_path):
    os.mkfifo(fifo_in_path)
if not os.path.exists(fifo_out_path):
    os.mkfifo(fifo_out_path)

# 启动读取线程
read_thread = threading.Thread(target=read_from_fifo)
read_thread.start()

# 启动写入线程
write_thread = threading.Thread(target=write_to_fifo)
write_thread.start()

# 执行 /challenge/run 并将 stdin 和 stdout 重定向到 FIFO
process = subprocess.Popen(['/challenge/run'], stdin=open(fifo_in_path, 'r'), stdout=open(fifo_out_path, 'w'))

# 等待挑战结束
process.wait()

# 等待线程完成
write_thread.join()
read_thread.join()

#fifo+简单运算
