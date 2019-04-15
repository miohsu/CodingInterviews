"""
    给你一段长度为 n 的绳子，请把绳子剪成 m 段(m, n 都是整数, n > 1 且 m > 1), 每段绳子的长度记为 k[0], k[1], ... , k[m].
    请问 k[0] * k[1] * k[2] * ... * k[m] 可能的最大乘积是多少？
    例如，当绳子的长度是 8 时我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18

"""


# 贪心算法实现

class Solution(object):

    def __init__(self, length, count):
        self.length = length
        self.count = count
        self.max = 0

    def max_products_after_cut(self):
        if self.length < 2:
            self.max = 0
        elif self.length == 2:
            self.max = 1
        elif self.length == 3:
            self.max = 2

        times_of_3, mod_of_3 = divmod(self.length, 3)
        if mod_of_3 == 1:
            times_of_3 -= 1
        times_of_2 = (self.length - times_of_3 * 3) // 2
        self.max = pow(3, times_of_3) * pow(2, times_of_2)


if __name__ == '__main__':
    res = Solution(8, 3)
    res.max_products_after_cut()
    print(res.max)
