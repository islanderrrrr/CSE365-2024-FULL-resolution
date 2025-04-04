# 挑战简介
```
GDB 是一种非常强大的动态分析工具，您可以使用它来了解程序在整个执行过程中的状态。您将在本模块中熟悉 gdb 的一些功能。

我们编写代码是为了表达一个可以重现和改进的想法。我们可以将我们的分析视为一个程序，它将要分析的目标作为数据注入。俗话说，代码就是数据，数据就是代码。

虽然像我们在之前的级别中所做的那样以交互方式使用 gdb 非常强大，但另一个强大的工具是 gdb 脚本。通过编写 gdb 脚本，您可以非常快速地创建定制的程序分析工具。如果您知道如何与 gdb 交互，那么您已经知道如何编写 gdb 脚本 - 语法完全相同。您可以将命令写入某个文件，例如 `x.gdb`，然后使用标志 `-x <PATH_TO_SCRIPT>` 启动 gdb。该文件将在 gdb 启动后执行所有 gdb 命令。或者，您可以使用 `-ex
'<COMMAND>'` 执行单个命令。您可以使用多个 `-ex` 参数传递多个命令。最后，您可以将某些命令放入 `~/.gdbinit` 中，让它们始终在任何 gdb 会话中执行。您可能希望在其中放入 `set disassembly-flavor
intel`。

在 gdb 脚本中，断点命令是一个非常强大的构造。考虑以下 gdb 脚本：

start
break *main+42
commands
x/gx $rbp-0x32
continue
end
continue

在这种情况下，每当我们命中 `main+42` 处的指令时，我们都会输出一个特定的局部变量，然后继续执行。

现在考虑一个类似但稍微高级一些的脚本，它使用了一些您还没有见过的命令：

start
break *main+42
commands
silent
set $local_variable = *(unsigned long long*)($rbp-0x32)
printf "Current value: %llx\n", $local_variable
continue
end
continue

在这种情况下，`silent` 表示我们希望 gdb 不报告我们已到达断点，以使输出更清晰一些。然后我们使用 `set` 命令在 gdb 会话中定义一个变量，其值是我们的本地变量。最后，我们使用格式化的字符串输出当前值。

使用 gdb 脚本帮助您收集随机值。

程序收到信号 SIGTRAP，跟踪/断点陷阱。
```

# 思路
其实这道题用上一题的思路一样可以解决，这次挑战是要求你在断点处设置命令索取寄存值并输出，老实说  
**我不懂！！！**  
所以我用上一题解法的优化解解决了  
只设置一个断点，在输入结果处，手动输入(悲  
**就这样吧**  
