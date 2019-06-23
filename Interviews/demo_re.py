"""
re 模块demo
"""
import re

pattern = '123'

result = []
with open('files/re_eg', 'r', encoding='utf8') as fp:
    data = fp.readline()
    while data:
        # result.append(re.findall(pattern, data))
        result.append(re.match(pattern, data))
        # result.append(re.fullmatch(pattern, data))
        data = fp.readline()

print(result)
