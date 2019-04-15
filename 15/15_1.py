"""
    输入一个整数，输出该数二进制表示中 1 的个数。
    例如，9 的二进制形式是 1001 有 2 个 1，则输出 2

    提示：
        二进制数 左移 都补 0; 右移 要注意：正数补 0 负数补 1
    注意：负数问题

    解决核心：
        原数字 - 1 and 原数字 == 最右边的 1 变为 0

"""


class Solution(object):
    def __init__(self, num):
        self._num = num
        self._count = 0

    def count_of_one(self):
        if self._num == 0:
            self._count = 0
        while self._num:
            if self._num:
                self._num = (self._num - 1) & self._num
                self._count += 1


if __name__ == '__main__':
    sol = Solution(11)
    sol.count_of_one()
    print(sol._count)
