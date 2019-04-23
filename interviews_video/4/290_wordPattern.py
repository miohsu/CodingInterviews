"""
给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
"""


class Solution:
    def wordPattern(self, pattern, str):
        """

        :param pattern: str
        :param str: str
        :return: bool
        """
        str_list = str.strip().split()
        if len(str_list) != len(pattern):
            return False
        map_dic = dict()
        for i, v in zip(pattern, str_list):
            if i not in map_dic:
                if v not in map_dic.values():
                    map_dic[i] = v
                else:
                    return False
            else:
                if map_dic[i] != v:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    pattern = "aaaa"
    str = "dog cat cat dog"
    pattern = "abba"
    str = "dog dog dog dog"
    print(sol.wordPattern(pattern, str))
