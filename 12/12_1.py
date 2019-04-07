"""
    矩阵中的路径
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
    路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上，下移动一格。
    如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
    例如，在下面的 3x4 的矩阵中包含一条字符串"bfce"的路径。
    但矩阵中不包含字符串"abfb"的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
"""


def has_path_core(data, rows, cols, row, col, search, path_length, visited):
    if path_length == len(search):
        return True

    in_path = False
    if 0 <= row < rows and 0 <= col < cols and data[row][col] == search[path_length] and \
            not visited[row][col]:
        path_length += 1
        visited[row][col] = True
        in_path = has_path_core(data, rows, cols, row - 1, col, search, path_length, visited) or \
                  has_path_core(data, rows, cols, row + 1, col, search, path_length, visited) or \
                  has_path_core(data, rows, cols, row, col - 1, search, path_length, visited) or \
                  has_path_core(data, rows, cols, row, col + 1, search, path_length, visited)
        if not in_path:
            path_length -= 1
            visited[row][col] = False
    return in_path


def has_path(data, rows, cols, search):
    result = False
    if not data or rows < 1 or cols < 1 or not search:
        return result

    visited = [[False] * cols for i in range(rows)]
    path_length = 0
    row = 0
    while row < rows:
        col = 0
        while col < cols:
            if has_path_core(data, rows, cols, row, col, search, path_length, visited):
                result = True
                return result
            col += 1
        row += 1
        return result


if __name__ == '__main__':
    data = [
        ['a', 'b', 't', 'g'],
        ['c', 'f', 'c', 's'],
        ['j', 'd', 'e', 'h'],
    ]
    # res = has_path(data, 3, 4, 'bfce')
    res = has_path(data, 3, 4, 'abfb')
    print(res)
