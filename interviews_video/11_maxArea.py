"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        max_area = (r - l) * min(height[r], height[l])
        while l < r:
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
            area = (r - l) * min(height[r], height[l])
            if area > max_area:
                max_area = area
        return max_area


if __name__ == '__main__':
    sol = Solution()
    data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = sol.maxArea(data)
    print(res)
