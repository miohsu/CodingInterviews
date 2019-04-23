"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""


class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left <= right:
            if not ('a' <= s[left] <= 'z' or 'A' <= s[left] <= 'Z' or '0' <= s[left] <= '9'):
                left += 1
                continue
            if not ('a' <= s[right] <= 'z' or 'A' <= s[right] <= 'Z' or '0' <= s[right] <= '9'):
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    data = "A man, a plan, a canal: Panama"
    data = "race a car"
    sol = Solution()
    print(sol.isPalindrome(data))
