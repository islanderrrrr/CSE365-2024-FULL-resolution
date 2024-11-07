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

正在从 /challenge/embryogdb_level1 读取符号...  
(在 /challenge/embryogdb_level1 中未找到调试符号)  
(gdb) run  
正在启动程序：/challenge/embryogdb_level1  
###  
### 欢迎来到 /challenge/embryogdb_level1！  
###

GDB 是一个非常强大的动态分析工具，您可以使用它来了解程序在整个执行过程中的状态。您将在本模块中熟悉 gdb 的一些功能。

您正在 gdb 中运行！程序当前已暂停。这是因为它在此处设置了自己的断点。

您可以使用命令“start”启动程序，并在“main”上设置断点。您可以使用命令 `starti` 来启动程序，并在 `_start` 上设置断点。您可以使用命令 `run` 来启动程序，而无需设置断点。您可以使用命令 `attach <PID>` 附加到其他已在运行的程序。您可以使用命令 `core <PATH>` 分析已运行程序的核心转储。

启动或运行程序时，您可以以几乎与在 shell 上完全相同的方式指定参数。  
例如，您可以使用 `start <ARGV1> <ARGV2> <ARGVN> < <STDIN_PATH>`。

使用命令 `continue`（简称 `c`）继续执行程序。
```

# 思路
根据语句执行命令即可  
就是教你用调试工具
