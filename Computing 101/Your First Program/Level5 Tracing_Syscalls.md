# 挑战简介
在编写大型程序时，可能会引入错误，这时调试工具就显得尤为重要。第一个工具是系统调用跟踪器strace。

strace可以记录程序调用的每一个系统调用及其结果。例如，运行以下命令：

bash
复制代码
strace /tmp/your-program
你会看到类似这样的输出：
```
arduino  
execve("/tmp/your-program", ["/tmp/your-program"], 0x7ffd48ae28b0 /* 53 vars */) = 0  
exit(42)                                 = ?
```
+++ exited with 42 +++  
这里，strace显示了程序触发的系统调用，包括参数和返回值。例如，exit(42)表示程序以状态码42退出。

虽然exit调用很容易查看，但其他系统调用（如alarm）就不那么明显。alarm系统调用设置一个定时器，当指定时间过去后，Linux会终止程序。在这个挑战中，你需要使用strace跟踪/challenge/trace-me程序，以找出它传递给alarm系统调用的参数值，然后将该值作为参数调用/challenge/submit-number。祝你好运！

# 思路:
**strace** 可以追踪系统调用的状态  
本题要求你用strace追踪**alarm**里的参数  
输入到一个程序里面
