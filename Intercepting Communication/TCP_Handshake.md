# 挑战简介
Manually perform a Transmission Control Protocol handshake

# 思路
```
#模拟TCP三次握手
#首先，Ether，IP，TCP的设置
#着重TCP的设置
tcp_layer = TCP(sport=31337, dport=31337, flags="S", seq=31337)

#数据包的发送与接受
syn_ack_packet = srp1(eth / ip_packet / tcp_layer, iface='eth0')  //用srp1要求具有eth的设置

#seq的设置和ack的设置
#注意，返回的seq会改变，而不是31337，卡了好久.
>>> ack_number = syn_ack_packet.seq + 1  //ack的设置即为seq+1
>>> seq_number = syn_ack_packet.ack
#第二步TCP的设置
tcp_layer = TCP(sport=31337, dport=31337, flags="A", seq=seq_number, ack=ack_number)

#对ack_packet设置
>>> ack_packet = eth / ip_packet / tcp_layer
#sendp发送后，标志握手成功
```
