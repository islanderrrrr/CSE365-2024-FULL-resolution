# 挑战简介
Manually send a Transmission Control Protocol packet

# 思路
The packet should have `TCP sport=31337, dport=31337, seq=31337, ack=31337, flags=APRSF`  多的要求  

思路就是创建一个tcp_layer,并进行设置，在进行连接，即可  
原来的基础上  
```
>>tcp_layer = TCP(sport=31337, dport=31337, seq=31337, ack=31337, flags="APRSF")
```
进行连接  
>>> packet = eth / ip_packet / tcp_layer  
即可  
