# 挑战简介
您的主机 10.0.0.1 正在端口 31337 上接收流量；请阻止该流量。

# 思路
防火墙的作用是什么，这题开始便会从一个iptables开始解答  
iptables的规则表和链：  
表（tables）提供特定的功能，iptables内置了4个表，即filter表、nat表、mangle表和raw表，分别用于实现包过滤，网络地址转换、包重构(修改)和数据跟踪处理。  
链（chains）是数据包传播的路径，每一条链其实就是众多规则中的一个检查清单，每一条链中可以有一条或数条规则。当一个数据包到达一个链时，iptables就会从链中第一条规则开始检查，  
看该数据包是否满足规则所定义的条件。如果满足，系统就会根据该条规则所定义的方法处理该数据包；否则iptables将继续检查下一条规则，如果该数据包不符合链中任一条规则，iptables就会根据该链预先定义的默认策略来处理数据包。  
此题目标端口31337  
# 阻止所有发往31337端口的TCP入站流量
sudo iptables -A INPUT -p tcp --dport 31337 -j DROP  

# 阻止所有发往31337端口的UDP入站流量
sudo iptables -A INPUT -p udp --dport 31337 -j DROP  

# 查看当前的iptables规则
sudo iptables -L -n -v  

出不来sudo去掉即可  
