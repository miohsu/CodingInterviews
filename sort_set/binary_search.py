"""
    二分查找法
"""


def binary_search(lst, target):
    if len(lst) == 0:
        return None

    l, r = 0, len(lst)  # [l, r)
    while l < r:
        mid = l + (r - l) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            l = mid + 1
        elif lst[mid] > target:
            r = mid
    return None


if __name__ == '__main__':
    data = [1, 3, 4, 6, 7, 9]
    target = 3
    print(binary_search(data, target))
