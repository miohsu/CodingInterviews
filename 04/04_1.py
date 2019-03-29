"""
    在一个二维数组中，每一行都按照从左到右依次递增，每一列从上到下依次递增。
    请完成一个函数，输入这样一个数组，和一个数，并判断数组装是否含有这个数。
    [[1,2,8,9],
     [2,4,9,12],
     [4,7,10,13],
     [6,8,11,15]
    ]
"""

exp = [[1, 2, 8, 9],
       [2, 4, 9, 12],
       [4, 7, 10, 13],
       [6, 8, 11, 15]
       ]


def is_contain(lst, num):
    if not lst or not lst[0]:
        return False

    rows = len(lst)
    columns = len(lst[0])

    row = 0
    col = columns - 1

    while row < rows and col >= 0:
        flag = lst[row][col]
        if num == flag:
            return True
        elif num < flag:
            col -= 1
        elif num > flag:
            row += 1

    return False


if __name__ == '__main__':
    test_list = [x for x in range(16)]
    for i in test_list:
        result = is_contain(exp, i)
        print("{} in exp is {}".format(i, result))
