"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
from math import fabs


class Solution:
    def threeSumClosest(self, nums, target):
        """

        :param nums:  List[int]
        :param target: int
        :return: int
        """
        from math import fabs
        if len(nums) < 3:
            return None
        nums.sort()
        compare_value = float('inf')
        result = None
        i = 0
        while i < len(nums) - 2:
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_value = nums[l] + nums[r] + nums[i]
                if current_value < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif current_value > target:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif current_value == target:
                    return target
                if compare_value > fabs(current_value - target):
                    compare_value = fabs(current_value - target)
                    result = current_value
            i += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 5, 10, 11]
    target = 12
    print(sol.threeSumClosest(nums, target))
