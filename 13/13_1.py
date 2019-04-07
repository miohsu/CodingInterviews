"""
    机器人的运动范围
    地上有一个 m 行 n 列的方格。
    一个机器人从坐标(0,0)的格子开始移动，它每次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和大于 k 的格子。
    例如，当 k 大于18时，机器人能够进入方格(35,37)，但是不能进入(35,38)因为 3+5+3+8=19,请问机器人能够到达多少个格子？
"""


def get_digital_sum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


def check(limit, rows, cols, row, col, visited):
    """

    :return: True or False
    """
    if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and get_digital_sum(row) + get_digital_sum(col) <= limit:
        return True
    return False


def move_count_core(limit, rows, cols, row, col, visited):
    count = 0
    if check(limit, rows, cols, row, col, visited):
        visited[row][col] = True
        count = 1 + move_count_core(limit, rows, cols, row - 1, col, visited) + \
                move_count_core(limit, rows, cols, row + 1, col, visited) + \
                move_count_core(limit, rows, cols, row, col - 1, visited) + \
                move_count_core(limit, rows, cols, row, col + 1, visited)
    return count


def move_count(limit, rows=10, cols=10):
    """

    :param limit: k
    :param rows: m
    :param cols: n
    :return: count
    """
    count = 0
    if limit < 0 or rows < 0 or cols < 0:
        return count
    visited = [[False] * cols for i in range(rows)]
    count = move_count_core(limit, rows, cols, 0, 0, visited)
    return count


if __name__ == '__main__':
    res = move_count(10)
    print(res)