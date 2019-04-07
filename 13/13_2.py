class Solution(object):
    def __init__(self, rows=10, cols=10):
        self._limit = 0
        self._rows = rows
        self._cols = cols
        self._visited = [[False] * cols for i in range(rows)]

    def _get_digital_sum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10
            number = number // 10
        return sum

    def _check(self, row, col):
        """

        :return: True or False
        """
        if 0 <= row < self._rows and 0 <= col < self._cols and not self._visited[row][col] and \
                self._get_digital_sum(row) + self._get_digital_sum(col) <= self._limit:
            return True
        return False

    def _move_count_core(self, row, col):
        count = 0
        if self._check(row, col):
            self._visited[row][col] = True
            count = 1 + self._move_count_core(row - 1, col) + \
                    self._move_count_core(row + 1, col) + \
                    self._move_count_core(row, col - 1) + \
                    self._move_count_core(row, col + 1)
        return count

    def move_count(self, limit):
        """

        :param limit: k
        :return: count
        """
        self._limit = limit
        count = 0
        if self._limit < 0 or self._rows < 0 or self._cols < 0:
            return count
        count = self._move_count_core(0, 0)
        return count


if __name__ == '__main__':
    solution = Solution()
    res = solution.move_count(limit=11)
    print(res)
