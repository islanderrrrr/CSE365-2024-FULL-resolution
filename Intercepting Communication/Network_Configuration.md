# 挑战简介
Hijack traffic from a remote host by configuring your network interface

# 思路
**要窥探其他ip地址的流量包信息**

要增加窥探的IP地址：
```
ip addr add <new-ip-address>/24 dev eth0
```
添加后用nc监听即可  
```
nc -lv port
```
