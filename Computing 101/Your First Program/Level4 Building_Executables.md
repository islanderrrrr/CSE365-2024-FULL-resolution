# 挑战简介
在这个挑战中，你将学习如何构建一个可执行程序。步骤如下：

编写汇编代码：将汇编代码写入文件（如asm.s），代码示例：
```
assembly  
.intel_syntax noprefix  
mov rdi, 42  
mov rax, 60  
syscall
```
***
.intel_syntax noprefix指示汇编器使用Intel语法。

汇编成目标文件：使用as命令将代码汇编为对象文件：
```
bash  
as -o asm.o asm.s
```
***
这将生成一个名为asm.o的对象文件。

链接为可执行文件：使用ld命令将对象文件链接为最终的可执行文件：
```
bash  
ld -o exe asm.o
```
***
这将创建一个名为exe的可执行文件。

运行可执行文件：运行exe并查看返回值：
```
bash  
./exe  
echo $?
```
***
你应该会得到42作为返回值。

注意，ld会发出关于入口符号_start的警告。如果你想消除这个警告，可以在代码中添加以下两行：
```
assembly  
.global _start  
_start:
```
***
这将定义一个全局的_start符号，指定程序的执行起始位置。

完成这些步骤后，构建你的可执行程序并将其传递给/challenge/check以获取标志！

# 思路:
上面基本上就是思路，把asm.s转变为asm.o,再转变为exe执行即可
