# 挑战简介
Monitor traffic from a remote host

# 思路 
这题开始我们就要用wireshark来扒取流量包了，运行/challenge/run后

在application中找到wireshark，进入流量活跃的窗口，寻找length长度为flag长度的流量包进行分析，即可
