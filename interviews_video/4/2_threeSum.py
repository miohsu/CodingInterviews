"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:
    def threeSum(self, nums):
        """

        :param nums: List[int]
        :return:List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        if nums[0] > 0 or nums[len(nums) - 1] < 0:
            return []
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == -nums[i]:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]

    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    # nums = [0, 0, 0]
    print(sol.threeSum(nums))
