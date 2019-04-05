"""
    旋转数组的最小数字
    把一个数组最开始的若干个元素搬运到数组的末尾，我们称之为旋转数组。输入一个旋转数组，输出旋转数组的最小值
"""


def order_search(lst, left, right):
    min_value = lst[left]
    for i in range(left, right + 1):
        if lst[i] < min_value:
            min_value = lst[i]
    return min_value


def cycle_min(lst):
    length = len(lst)
    if length <= 1:
        return lst
    left, right = 0, length - 1
    mid = left
    while lst[left] >= lst[right]:
        if right - left == 1:
            mid = right
            break
        mid = (right - left) // 2 + left
        if lst[mid] == lst[left] == lst[right]:
            return order_search(lst, left, right)

        if lst[mid] >= lst[left]:
            left = mid
        elif lst[mid] <= lst[right]:
            right = mid
    return lst[mid]


if __name__ == '__main__':
    # lst = [3, 4, 5, 1, 2]
    lst = [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    result = cycle_min(lst)
    print(result)
