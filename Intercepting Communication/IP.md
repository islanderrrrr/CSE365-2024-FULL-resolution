# 挑战简介
Manually send an Internet Protocol packet

# 思路
这次要设置internet协议数据包  
`IP proto=0xFF`  
IP proto（IP protocol）是指 IP 数据包中的协议字段，它指定了数据包的有效负载使用的上层协议类型。在 IP 头部中，proto 字段占 8 位，用来表明该数据包传递的数据属于哪种网络协议，比如 TCP、UDP 等。  
因此，当你设置 IP proto=0xFF 时，实际上你是告诉接收端，这个数据包的协议类型是一个用户定义的协议 255。  
```
scapy -H
eth = Ether(src="fe:1b:61:25:dd:9b")
ip_packet = IP(dst="10.0.0.3", proto=0xFF)
packet = eth / ip_packet
#eth / ip_packet：使用 / 将 eth（以太网层）和 ip_packet（IP层）叠加在一起，构建一个完整的数据包。这意味着：
```

**以太网层作为数据包的最底层，负责局域网内的数据传输。** 
**IP 层是上层协议，负责在网络中路由和寻址。**  
**当你执行 eth / ip_packet 时，Scapy 自动处理将 ip_packet 嵌套到 eth 之后，生成完整的数据包。**  
```
sendp(ip_packet,iface="eth0")
```
