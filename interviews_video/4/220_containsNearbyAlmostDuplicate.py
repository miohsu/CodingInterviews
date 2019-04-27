"""
给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false
"""

import math


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """

        :param nums: List[int]
        :param k: int
        :param t: int
        :return: bool
        """
        if len(nums) < 2:
            return False
        l, r = 0, 1
        num_set = {nums[0], }
        while r < len(nums):
            if r - l <= k:
                if t != 0:
                    for value in num_set:
                        if math.fabs(nums[r] - value) <= t:
                            return True
                else:
                    if nums[r] in num_set:
                        return True
                num_set.add(nums[r])
                r += 1
            else:
                num_set.remove(nums[l])
                l += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3
    nums = [1, 0, 1, 1]
    k = 1
    t = 2
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(sol.containsNearbyAlmostDuplicate(nums, k, t))
