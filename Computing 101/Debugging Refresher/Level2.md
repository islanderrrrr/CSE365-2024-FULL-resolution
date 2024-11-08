# 挑战简介
```
程序正在 gdb 的控制下重新启动！您可以使用 gdb 命令“run”运行该程序。

GNU gdb (Ubuntu 9.2-0ubuntu1~20.04.2) 9.2
版权所有 (C) 2020 Free Software Foundation, Inc.
许可证 GPLv3+：GNU GPL 版本 3 或更高版本 <http://gnu.org/licenses/gpl.html>
这是免费软件：您可以自由更改和重新分发它。
在法律允许的范围内，没有任何担保。
输入“show copying”和“show warranties”了解详情。
此 GDB 配置为“x86_64-linux-gnu”。
输入“show configuration”了解配置详情。
有关错误报告说明，请参阅：
<http://www.gnu.org/software/gdb/bugs/>。
在线查找 GDB 手册和其他文档资源：
<http://www.gnu.org/software/gdb/documentation/>。

如需帮助，请键入“help”。
键入“apropos word”以搜索与“word”相关的命令...
正在从 /challenge/embryogdb_level2 读取符号...
（在 /challenge/embryogdb_level2 中未找到调试符号）
（gdb）c
程序未运行。
（gdb）start
临时断点 1 位于 0x1aa6
正在启动程序：/challenge/embryogdb_level2

临时断点 1，main () 中的 0x000058bb6dfa0aa6
（gdb）c
继续。
###
### 欢迎来到 /challenge/embryogdb_level2！
###

GDB 是一个非常强大的动态分析工具，您可以使用它来了解程序在整个执行过程中的状态。您将在本模块中熟悉 gdb 的一些功能。

您可以使用“info registers”查看所有寄存器的值。或者，您也可以使用“print”命令（简称为“p”）打印特定寄存器的值。例如，“p $rdi”将以十进制打印 $rdi 的值。您还可以使用“p/x $rdi”以十六进制打印其值。

为了解决这一关，您必须找出寄存器 r12 的当前十六进制随机值。

随机值已设置！

程序收到信号 SIGTRAP，跟踪/断点陷阱。

0x000058bb6dfa0bfd 在 main ()
(gdb) c
继续。
随机值：
```

# 思路
这里教你使用gdb调试打印输出十进制十六进制  
没啥说的。
