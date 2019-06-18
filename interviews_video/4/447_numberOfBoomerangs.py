"""
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""


class Solution:
    def numberOfBoomerangs(self, points):
        """

        :param points:  List[List[int]]
        :return: int
        """

        result = 0
        for index, (xi, yi) in enumerate(points):
            l = 0
            d = dict()
            while l < len(points):
                if l == index:
                    l += 1
                    continue
                x, y = points[l]
                distance = pow(x - xi, 2) + pow(y - yi, 2)
                if distance not in d:
                    d[distance] = 1
                else:
                    d[distance] += 1
                l += 1
            for point_list in d.values():
                result += point_list * (point_list - 1)
        return result


if __name__ == '__main__':
    sol = Solution()
    data = [[0, 0], [1, 0], [2, 0]]
    print(sol.numberOfBoomerangs(data))
