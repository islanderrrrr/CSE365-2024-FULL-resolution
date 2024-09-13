exec 18<test1;/challenge/run

# exec 是一个 shell 内置命令，用于在当前 shell 环境中执行命令，而不会启动新的子进程。exec 也可以用来改变文件描述符的配置。
18<test1 表示将文件描述符 18 与 FIFO test1 相关联，并且是用于读取（< 表示输入重定向）。这意味着从此之后，文件描述符 18 将读取 test1 中的数据。
