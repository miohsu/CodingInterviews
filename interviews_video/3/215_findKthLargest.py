"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
import random


class Solution:
    def partation(self, nums, left, right):
        r_index = random.randint(left, right - 1)
        nums[left], nums[r_index] = nums[r_index], nums[left]
        flag = nums[left]
        i, j = left, right - 1
        while i < j:
            while i < j and nums[j] <= flag:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] > flag:
                i += 1
            nums[j] = nums[i]
        nums[i] = flag
        return i

    def findKthLargest(self, nums, k):
        if len(nums) == 0 or len(nums) < k:
            return None
        left, right = 0, len(nums)
        while left < right:
            mid = self.partation(nums, left, right)  # 返回标定点的index
            if mid == k - 1:
                return nums[mid]
            elif mid > k - 1:
                right = mid
            elif mid < k - 1:
                left = mid + 1


if __name__ == '__main__':
    sol = Solution()
    # nums = [3, 2, 1, 5, 6, 4]
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    # k = 2
    res = sol.findKthLargest(nums, k)
    print(res)
