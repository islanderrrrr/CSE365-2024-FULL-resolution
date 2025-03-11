# 挑战简介
您的主机 10.0.0.1 正在端口 31337 上接收流量；阻止该流量，但仅阻止来自远程主机 10.0.0.3 的流量，您必须允许来自远程主机 10.0.0.2 的流量。

# 思路
语法题，意思很明确

# 允许来自10.0.0.2的流量访问31337端口（放在前面优先匹配）
sudo iptables -A INPUT -s 10.0.0.2 -p tcp --dport 31337 -j ACCEPT
sudo iptables -A INPUT -s 10.0.0.2 -p udp --dport 31337 -j ACCEPT

# 阻止来自10.0.0.3的流量访问31337端口
sudo iptables -A INPUT -s 10.0.0.3 -p tcp --dport 31337 -j DROP
sudo iptables -A INPUT -s 10.0.0.3 -p udp --dport 31337 -j DROP
