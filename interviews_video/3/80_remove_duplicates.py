"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定 nums = [1,1,1,2,2,3],
函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,1,2,3,3],
函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        l, k, r = 1, 0, len(nums)
        same_flag = False
        while l < r:
            if nums[k] != nums[l] or not same_flag:
                if nums[k] == nums[l]:
                    same_flag = True
                else:
                    same_flag = False
                k += 1
                if k != l:
                    nums[k] = nums[l]
            l += 1
        return k + 1


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    res = sol.removeDuplicates(nums)
    print(res, nums)
