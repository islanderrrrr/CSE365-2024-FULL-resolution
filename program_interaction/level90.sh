#创建FIFO通道：
mkfifo test
#写入shell脚本，是读方
echo '/challenge/run < test' > intera_script.sh
#同时运行读写进程，所以需要用算数运算符|或&进行连接，注意不能用分号;，因为那样是串行执行：
echo bnswyafr > test | bash intera_script.sh
