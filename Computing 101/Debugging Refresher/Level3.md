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

从 /challenge/embryogdb_level3 读取符号...
(在 /challenge/embryogdb_level3 中未找到调试符号)
(gdb) start
临时断点 1 位于 0x1aa6
启动程序：/challenge/embryogdb_level3

临时断点 1，0x00005f2675523aa6 在 main ()
(gdb) c
继续。
###
### 欢迎来到 /challenge/embryogdb_level3！
###

GDB 是一个非常强大的动态分析工具，您可以使用它来了解程序在整个执行过程中的状态。您将在本模块中熟悉 gdb 的一些功能。

您可以使用 `x/<n><u><f> <address>` 参数化命令检查内存的内容。在此格式中，`<u>` 是要显示的单元大小，`<f>` 是显示格式，`<n>` 是要显示的元素数。有效的单元大小为 `b`（1 字节）、`h`（2 字节）、`w`（4 字节）和 `g`（8 字节）。有效格式为 `d`（十进制）、`x`
（十六进制）、`s`（字符串）和 `i`（指令）。可以使用寄存器名称、符号名称或
绝对地址指定地址。此外，您还可以在指定地址时提供数学表达式。

例如，`x/8i $rip` 将从当前指令指针打印接下来的 8 条指令。`x/16i main` 将
打印 main 的前 16 条指令。您还可以使用 `disassemble main`（简称 `disas main`）来打印 main 的所有
指令。或者，`x/16gx $rsp` 将打印堆栈上的前 16 个值。`x/gx $rbp-0x32`
将打印堆栈上存储的局部变量。

您可能希望使用正确的汇编语法查看您的指令。您可以使用命令
`set disassembly-flavor intel` 来执行此操作。

为了解决这一关，您必须找出堆栈上的随机值（从 `/dev/urandom` 读入的值）。
考虑一下 read 系统调用的参数是什么。

程序收到信号 SIGTRAP，跟踪/断点陷阱。
```

# 思路
搞不懂搞不懂，要我们找出随机数，用(gdb) x/16gx $rsp发现第3行地址存储的随机数(why)  
```
(gdb) x/gx $rbp-0x32
0x7ffd17392eae: 0x7ffd17392fd80000
(gdb) x/16gx $rsp
0x7ffd17392ea0: 0x0000000000000002      0x00007ffd17392fe8
0x7ffd17392eb0: 0x00007ffd17392fd8      0x000000018d507d10
0x7ffd17392ec0: 0x0000000000000000      0xe9f1133f424a1b6e
0x7ffd17392ed0: 0x00007ffd17392fd0      0x1976488e34b1e900
0x7ffd17392ee0: 0x0000000000000000      0x00007ab0495ec083
0x7ffd17392ef0: 0x00007ab0497f8620      0x00007ffd17392fd8
0x7ffd17392f00: 0x0000000100000000      0x0000601e8d507aa6
0x7ffd17392f10: 0x0000601e8d507d10      0x065b7c87737c54ac
(gdb) c
Continuing.
Random value: e9f1133f424a1b6e
You input: e9f1133f424a1b6e
The correct answer is: e9f1133f424a1b6e
You win! Here is your flag:
```
**来个哥们解释一下**
