"""
regex2.py
match 对象属性演示
"""

import re

pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search('abcdefghij')  # match属性对象

# 属性对象
print(obj.pos)  # 目标字符串开始位置
print(obj.endpos) # 目标字符串结尾位置
print(obj.re) # 正则表达式
print(obj.string) # 目标字符串
print(obj.lastgroup) # 最后一组组名
print(obj.lastindex) # 最后一组序列号

# 属性方法
print("====================")
print(obj.span()) # 匹配内容在字符串位置
print(obj.start())
print(obj.end())
print(obj.groupdict()) # 生成捕获组字典
print(obj.groups()) # 子组对应内容元组
print(obj.group()) # 获取match对象对应的内容