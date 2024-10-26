# 挑战简介
***
前面的都是答题，现在也是答题，只不过这一次，你要用**1秒钟答对20个题**
***

# 那么思路是什么？
## 我们需要创造一个脚本
这个脚本要做到:
1. 储存所有等级和类别，对于等级要进行大小的区别
2. 本地程序，需要做好本地信息的识别与回复。
3. 题目的回答:
  1. 对于读操作，需要保证主体等级大于等于客体等级，主体的类别需要包含客体的类别
  2. 对于写操作，需要保证主体等级小于等于客体等级，客体的类别需要包含客体的类别  
**以上便是全部问题**
***
```
#!/usr/bin/python
import re    #re模块，关于正则表达式
from pwn import *    #pwntools

levels = {'TS': 4, 'S': 3, 'C': 2, 'UC': 1}    #等级分层
categories = ['UFO', 'NATO', 'ACE', 'NUC']      #所有类别

def can_read(subject_level, subject_categories, object_level, object_categories):    #定义read模块
    if levels[subject_level] < levels[object_level]:      #对比等级
        return False
    if not set(object_categories).issubset(set(subject_categories)):      如果主体不包含客体所有类别
        return False
    return True

def can_write(subject_level, subject_categories, object_level, object_categories):    #定义write模块
#    print(subject_level)
#    print(subject_categories)
#    print(object_level)
#    print(object_categories)
    if levels[subject_level] > levels[object_level]:    #对比等级
        return False

#    if not object_categories:
#        return True

    if not set(subject_categories).issubset(set(object_categories)):    #如果客体不包含主体所有类别
        return False

    return True

context(os='linux',arch='AMD64',log_level='debug')    #调试以及参数
p = process('/challenge/run')    #运行指定路径
def answer_master(question):      #分解问题以及提取参数
        match = re.search(
            r'level (\w+) and categories \{([^}]*)\} (read|write) an Object with level (\w+) and categories \{([^}]*)\}', question
        )

        if match:
            sub_level = match.group(1)      #获取主体级别
            sub_categories = match.group(2).strip()      #获取主体类别
            if sub_categories:    #判断是否为空集
                sub_categories = sub_categories.split(', ')    #分割以','
            else:
                sub_categories = []      #赋予空值
                
            action = match.group(3)     #获取操作 (read或write)
            obj_level = match.group(4)      #获取客体级别
            obj_categories = match.group(5).strip()    
            if obj_categories:    #同上
                obj_categories = obj_categories.split(', ')
            else:
                obj_categories = []

            return sub_level, sub_categories, obj_level, obj_categories, action    返回5个参数

        return None
#        p.recvuntil("Q ")       
#        response = p.recvline("Q ")     #获取客体
#        response = response.decode()
#        parts = response.split()
#        sub_level = parts[6]        #获取主体级别
#        sub_categories = parts[9].strip('{}').split(',')       #获取主体分类
#        response_la = p.recvuntil("} ")
#        obj_level = parts[10]
#        print(response_la)
#        p.sendline("yes")

while True:
    question = p.recvline().decode().strip()    #接收每一条返回信息
    print(f"Question: {question}")

    parsed_result = answer_master(question)
    if parsed_result is None:
        print("Fail to parse question")
        continue

    subject_level, subject_categories, object_level, object_categories, action = parsed_result

    if action == "read":      
        result = can_read(subject_level, subject_categories, object_level, object_categories)
    elif action == "write":
        result = can_write(subject_level, subject_categories, object_level, object_categories)
    else:
        print("Unknown action")
        continue

    if result:
        p.sendline("yes")
    else:
        p.sendline("no")

    print(f"Answer: {'yes' if result else 'no'}")

p.close()
    
answer_master(20)
```
