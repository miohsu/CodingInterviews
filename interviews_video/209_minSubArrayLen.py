"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
"""


class Solution:
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        l, r = 0, 0
        length = len(nums)
        min_len = length + 1
        tmp_sum = 0
        while r < length:
            tmp_sum += nums[r]
            while tmp_sum >= s and l <= r:
                min_len = min(min_len, (r - l + 1))
                if min_len == 1:
                    return min_len
                tmp_sum -= nums[l]
                l += 1
            r += 1

        if min_len > length:
            return 0
        return min_len

    def binary_search(self, lst, target, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if target > lst[mid]:
                left = mid + 1
            elif target < lst[mid]:
                right = mid
            else:
                return mid + 1
        return right

    def minSubArrayLen_2(self, s, nums):
        if len(nums) == 0:
            return 0
        sums = []
        tmp = 0
        for val in nums:
            tmp += val
            sums.append(tmp)
        if s > sums[-1]:
            return 0
        elif s == sums[-1]:
            return len(sums)
        len_min = len(sums) + 1
        for index, value in enumerate(sums):
            if value >= s:
                pos = self.binary_search(sums, sums[index] - s, 0, len(nums))
                len_min = min(len_min, (index - pos + 1))
        return len_min


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    sol = Solution()
    # res = sol.minSubArrayLen(s, nums)
    # print(res)
    res = sol.minSubArrayLen_2(s, nums)
    print(res)
