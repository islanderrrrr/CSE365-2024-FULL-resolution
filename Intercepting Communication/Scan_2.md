# 挑战简介
Find and connect to a remote host on a large network

# 思路
有点逆天，是上一道题的加强版，从256个端口直接256^2倍，这时候我们就要想办法提高nmap的效率，因为这道题不涉及防火墙，所以我们可以尽情加快速度。
nc -p 31337 -T5 --min-rate 1000 10.0.0.0/16

**-T5是最快搜索速度，容易被防火墙直接发现，一般不建议。T0-T5为范围**

**--min-rate最小扫描速率，我们可以设置1000，这是提高速度的关键解**
