# 挑战简介
GDB 是一个非常强大的动态分析工具，您可以使用它来了解程序在整个执行过程中的状态。您将在本模块中熟悉 gdb 的一些功能。

正如我们在上一个级别中演示的那样，gdb 可以完全控制目标进程。在正常情况下，以普通用户身份运行的 gdb 无法附加到特权进程。这就是为什么 gdb 不是一个大的安全问题，它允许您立即解决所有级别。尽管如此，gdb 仍然是一个非常强大的工具。

在这个提升的 gdb 实例中运行可以让您提升对整个系统的控制。为了清楚地演示这一点，看看当您运行命令 `call (void)win()` 时会发生什么。事实证明，本模块中的所有级别都可以通过这种方式解决。

GDB 非常强大！

程序收到信号 SIGTRAP，跟踪/断点陷阱。

# 思路
这题就是教你在gdb里面call函数，call完就是flag

**无**
