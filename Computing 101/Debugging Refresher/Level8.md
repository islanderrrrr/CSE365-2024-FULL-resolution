# 挑战简介
```
GDB 是一个非常强大的动态分析工具，您可以使用它来了解程序在整个执行过程中的状态。您将在本模块中熟悉 gdb 的一些功能。

正如我们在上一个级别中演示的那样，gdb 可以完全控制目标进程。在正常情况下，以普通用户身份运行的 gdb 无法附加到特权进程。这就是为什么 gdb 不是一个可以立即解决所有级别的大规模安全问题的原因。尽管如此，gdb 仍然是一个非常强大的工具。

在这个提升的 gdb 实例中运行可以让您提升对整个系统的控制。为了清楚地演示这一点，请查看运行命令“call (void)win()”时会发生什么。

请注意，这不会为您带来标志（似乎我们破坏了 win 函数！），因此您需要更加努力才能获得此标志！

事实证明，模块中的所有其他级别都可以通过这种方式解决。

GDB 非常强大！

程序收到信号SIGTRAP，跟踪/断点陷阱。
```
# 思路
这一题和上一题也类似，只不过这一次win函数里面参杂了一些影响你获取flag的语句，所以这一次，你可以尝试用jump来实现
- 利用jump跳转到win函数，进行ni排查
- 发现报错的语句时，继续往后面逐个字节break排查，直至无报错
- 无报错时，正常执行后面的语句，即可获取flag

**完结撒花**