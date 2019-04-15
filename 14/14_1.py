"""
    给你一段长度为 n 的绳子，请把绳子剪成 m 段(m, n 都是整数, n > 1 且 m > 1), 每段绳子的长度记为 k[0], k[1], ... , k[m].
    请问 k[0] * k[1] * k[2] * ... * k[m] 可能的最大乘积是多少？
    例如，当绳子的长度是 8 时我们把它剪成长度分别为 2、3、3 的三段，此时得到的最大乘积是 18

"""


# 动态规划实现

class Solution(object):
    def __init__(self, length, count):
        self.length = length
        self.count = count
        self.max = 0
        self.products = {0: 0, 1: 1, 2: 2, 3: 3}

    def product_after_cutting(self):
        if self.length < 2:
            return 0
        elif self.length == 2:
            return 1
        elif self.length == 3:
            return 2

        i = 4
        while i <= self.length:
            cut = 1
            while cut <= i // 2:
                max = 0
                max = self.products[cut] * self.products[i - cut]
                if max > self.max:
                    self.max = max
                cut += 1
            self.products[i] = self.max
            i += 1


if __name__ == '__main__':
    res = Solution(*[8, 3])
    # print(res.product_after_cutting())
    res.product_after_cutting()
    print(res.products)
