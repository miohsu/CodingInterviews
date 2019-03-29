"""
    请实现一个函数，把字符串中的每个空格替换成"%20".
    例如，输入"We are family.", 则输出"We%20are%20family."
"""
import re


# 遍历 O(n)
def change_space(change_str, new_sub_str):
    if not change_str:
        return change_str
    change_str = list(change_str)
    new_sub_str = list(new_sub_str)
    length = len(change_str)
    change_counts = []

    index = 0
    while index < length:
        if change_str[index] == ' ':
            start = index
            while index < length:
                if change_str[index] != ' ':
                    break
                index += 1
            change_counts.append((start, index))
        else:
            index += 1
    while change_counts:
        start, end = change_counts.pop()
        change_str[start:end] = new_sub_str
    return ''.join(change_str)


# 基于正则
def re_method(change_str, new_sub_str):
    if not change_str:
        return change_str
    change_str = re.sub('\s+', new_sub_str, change_str)
    return change_str


def list_method(change_str, new_sub_str):
    if not change_str:
        return change_str
    head = tail = False
    if change_str[0] == ' ':
        head = True
    if change_str[-1] == ' ':
        tail = True

    change_str = change_str.split()
    change_str = [x for x in change_str if x != '']
    change_str = new_sub_str.join(change_str)
    if head:
        change_str = new_sub_str + change_str
    if tail:
        change_str += new_sub_str
    return change_str


if __name__ == '__main__':
    change_str = " We are   family.  "
    # result = change_space(change_str, '#')
    # result = re_method(change_str, '#')
    result = list_method(change_str, '#')
    print(result)
