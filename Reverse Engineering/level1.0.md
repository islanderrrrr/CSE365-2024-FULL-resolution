# 挑战简介
此许可证验证软件允许您读取该标志。但是，在此之前，您必须验证您是否有权读取标志文件！此程序通过标准输入使用许可证密钥。每个程序可能对该输入执行完全不同的操作！
您必须（通过对该程序进行逆向工程）找出该许可证密钥。
提供正确的许可证密钥即可获得该标志！

# 思路
逆向思路还是挺清楚的，寻求key我们就直接用IDA去查找其cmp函数，查看对比的expected_result，便可得到提取数据  
**ajznh**  
运行程序，输入密钥就得出了  
```
hacker@reverse-engineering~level1-0:~$ /challenge/babyrev-level-1-0

###
### Welcome to /challenge/babyrev-level-1-0!
###

This license verifier software will allow you to read the flag. However, before you can do so, you must verify that you
are licensed to read flag files! This program consumes a license key over stdin. Each program may perform entirely
different operations on that input! You must figure out (by reverse engineering this program) what that license key is.
Providing the correct license key will net you the flag!

Ready to receive your license key!

ajznh
```
