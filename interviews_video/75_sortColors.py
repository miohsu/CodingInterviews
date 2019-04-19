"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""
import random


class Solution:
    def sortColors(self, nums):
        if len(nums) == 0:
            return nums
        stat = {
            0: 0,
            1: 0,
            2: 0,
        }
        for i in nums:
            stat[i] += 1
        n = 0
        while n < len(nums):
            for i in range(stat[0]):
                nums[n] = 0
                n += 1
            for i in range(stat[1]):
                nums[n] = 1
                n += 1
            for i in range(stat[2]):
                nums[n] = 2
                n += 1

        return nums

    def sortColor_2(self, nums):
        length = len(nums)
        if length < 2:
            return
        l, r = 0, length
        flag = 1
        lt, gt = l - 1, r
        i = l
        while i < gt:
            if nums[i] < flag:
                nums[i], nums[lt + 1] = nums[lt + 1], nums[i]
                lt += 1
                i += 1
            elif nums[i] > flag:
                nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
                gt -= 1
            else:
                i += 1


if __name__ == '__main__':
    data = [1, 2, 2, 2, 2, 0, 0, 0, 1, 1]
    data = [2, 0, 1]
    sol = Solution()
    # res = sol.sortColors(data)
    res = sol.sortColor_2(data)
    print(data)
