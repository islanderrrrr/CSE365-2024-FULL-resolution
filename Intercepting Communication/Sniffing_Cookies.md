# 挑战简介
您已经学会了嗅探流量，但知识只是行动的开始。现在是时候将其应用于实际的安全场景了。窃取管理员的 cookie，并获取标志！

提示：您可以使用您在 Talking Web 中学习的全套 HTTP 工具来使用窃取的 cookie！但无论您做什么，请确保在 10.0.0.1 终端中执行，以确保您在正确的主机上运行！
您可以在后台运行 Wireshark 或其他您需要的程序（如您在 The Linux Luminarium 中学到的）。

# 思路
此题相对综合，你要通过wireshark查看本机ip对10.0.0.2访问的记录，获取cookie，从而对网站进行flag窃取

- 利用wireshark查找cookie
- curl访问输入报文cookie头
- 从记录可知，10.0.0.2/ping这个目录下会有回显，所以你不妨试试flag目录

