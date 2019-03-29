"""
    请实现一个函数，把字符串中的每个空格替换成"%20".
    例如，输入"We are family.", 则输出"We%20are%20family."
"""


def change_space(change_str, new_sub_str):
    if not change_str:
        return change_str
    change_str = list(change_str)
    new_sub_str = list(new_sub_str)
    space_dict = dict()
    length = len(change_str)
    for i in range(length):
        if change_str[i] == ' ':
            if i in space_dict:
                space_dict[i] += 1
            else:
                space_dict[i] = 1
    for key, value in space_dict.items():
        change_str[key:key + value] = new_sub_str
    return ''.join(change_str)


if __name__ == '__main__':
    change_str = "We are family."
    # result = list(change_str)
    result = change_space(change_str, '%20')
    print(result)
