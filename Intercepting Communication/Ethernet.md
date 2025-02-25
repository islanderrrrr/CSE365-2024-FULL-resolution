# 挑战简介
Manually send an Ethernet packet

# 思路
发送数据包的题，我们要认识一个新的语法  
scapy  

Scapy 是一个 Python 程序，它使用户能够发送、嗅探、剖析和伪造网络数据包。此功能允许构建可以探测、扫描或攻击网络的工具。  
换句话说，Scapy 是一个强大的交互式数据包操作程序。它能够伪造或解码多种协议的数据包，通过网络发送它们，捕获它们，匹配请求和回复等等。  
Scapy 可以轻松处理大多数经典任务，例如扫描、跟踪路由、探测、单元测试、攻击或网络发现。它可以替代 hping、arpspoof、arp-sk、arping、p0f 甚至 Nmap、tcpdump 和 tshark 的某些部分。                          

所以  
```
scapy -H
>>eth = Ether(src="d2:56:cd:9a:7b:27", type=0xFFFF)  //des目的地不用写，因为已经默认存在，你只需要输入自己的mac地址即可
>>sendp(eth, iface="eth0")  //iface:网卡名称
```

**查看自己的mac地址：**
```
ether 后面跟着的就是 MAC 地址：
link/ether d2:56:cd:9a:7b:27
```
