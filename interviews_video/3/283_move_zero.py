"""
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        输入: [0,1,0,3,12]
        输出: [1,3,12,0,0]

    说明:
        必须在原数组上操作，不能拷贝额外的数组。
        尽量减少操作次数。
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        assert len(nums) != 0
        l, k = 0, 0
        length = len(nums)
        while l < length:
            if nums[l] != 0:
                if k != l:
                    nums[k] = nums[l]
                k += 1
            l += 1
        while k < length:
            nums[k] = 0
            k += 1


if __name__ == '__main__':
    data = [0, 1, 0, 3, 12, 0]
    sol = Solution()
    sol.moveZeroes(data)
    print(data)
