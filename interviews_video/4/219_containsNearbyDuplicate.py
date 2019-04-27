"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """

        :param nums:  List[int]
        :param k: int
        :return: bool
        """
        if k < 1 or len(nums) < 2 or len(nums) == len(set(nums)):
            return False
        num_set = {nums[0], }
        l, r = 0, 1
        while r < len(nums):
            if r - l <= k:
                if nums[r] in num_set:
                    return True
                else:
                    num_set.add(nums[r])
                    r += 1
            else:
                num_set.remove(nums[l])
                l += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    nums = [1, 2, 3, 1, 2, 3]
    k = 2
    print(sol.containsNearbyDuplicate(nums, k))
