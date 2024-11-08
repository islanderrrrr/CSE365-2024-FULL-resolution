# 挑战简介
```
GDB 是一个非常强大的动态分析工具，您可以使用它来了解程序在执行过程中的状态。您将在本模块中熟悉 gdb 的一些功能。

动态分析的一个关键部分是让您的程序处于您想要分析的状态。到目前为止，这些挑战已经自动为您设置了断点，以便在您可能想要分析的状态暂停执行。
能够自己做到这一点很重要。

有多种方法可以推进程序的执行。您可以使用 `stepi <n>` 命令，或简称 `si <n>`，来前进一条指令。您可以使用 `nexti <n>` 命令，或简称 `ni <n>`，来前进一条指令，同时跳过任何函数调用。
`<n>` 参数是可选的，但允许您一次执行多个步骤。您可以使用 `finish` 命令来完成当前正在执行的函数。您可以使用 `break *<address>` 参数化命令在指定地址处设置断点。您已经使用了 `continue` 命令，该命令将继续执行，直到程序到达断点。

在逐步执行程序时，您可能会发现始终显示一些值很有用。有多种方法可以做到这一点。最简单的方法是使用 `display/<n><u><f>` 参数化命令，其格式与 `x/<n><u><f>` 参数化命令完全相同。
例如，`display/8i $rip` 将始终向您显示接下来的 8 条指令。另一方面，`display/4gx $rsp` 将始终向您显示堆栈上的前 4 个值。
另一个选项是使用 `layout regs` 命令。这将使 gdb 进入其 TUI 模式并向您显示所有寄存器的内容以及附近的指令。

为了解决这一关，您必须找出一系列将被放置在堆栈上的随机值。强烈建议您尝试使用 `stepi`、`nexti`、`break`、`continue` 和 `finish` 的组合，以确保您对这些命令有很好的内部理解。这些命令对于导航程序的执行都至关重要。

程序收到信号 SIGTRAP、跟踪/断点陷阱。
```

# 思路
这题有点意思，教你如何使用断点  
几个注意点
- 设置断点用break *address，设置断点后，用c则会直接跳转到下一个断点
- 循环体结构设置断点才不会一次运行完毕
- 可以利用display/8i $rip对地址运行进行动态观测，display/8xg $rsp来对堆栈进行监测
- 用ni辅助进行断点设置

```
#随机数生成断点2设置
(gdb) break *0x5cdd97a9acb7
Breakpoint 2 at 0x5cdd97a9acb7
```

```
#输入断点3设置
(gdb) ni
dad50fb35d51a453
0x00005cdd97a9ace0 in main ()
1: x/8xg $rsp
0x7ffebc495200: 0x0000000000000002      0x00007ffebc495348
0x7ffebc495210: 0x00007ffebc495338      0x0000000197a9ad60
0x7ffebc495220: 0x0000000000000000      0xdad50fb35d51a453
0x7ffebc495230: 0xdad50fb35d51a453      0xb7e6da60c06e9700
2: x/8i $rip
=> 0x5cdd97a9ace0 <main+570>:   mov    -0x10(%rbp),%rax
   0x5cdd97a9ace4 <main+574>:   mov    %rax,%rsi
   0x5cdd97a9ace7 <main+577>:   lea    0xe1e(%rip),%rdi        # 0x5cdd97a9bb0c
   0x5cdd97a9acee <main+584>:   mov    $0x0,%eax
   0x5cdd97a9acf3 <main+589>:   callq  0x5cdd97a9a1d0 <printf@plt>
   0x5cdd97a9acf8 <main+594>:   mov    -0x18(%rbp),%rax
   0x5cdd97a9acfc <main+598>:   mov    %rax,%rsi
   0x5cdd97a9acff <main+601>:   lea    0xe17(%rip),%rdi        # 0x5cdd97a9bb1d
(gdb) break *0x5cdd97a9acdb
Breakpoint 3 at 0x5cdd97a9acdb
```

**后面不断continue即可，随机数就是第三排第三列的16进制数**
