"""
    归并排序
"""
from sort_set.create_data import create_data


def merge(left, right):
    i, j = 0, 0
    l_len = len(left)
    r_len = len(right)
    result = []
    while i < l_len and j < r_len:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < l_len:
        result.extend(left[i:])
    elif j < r_len:
        result.extend(right[j:])
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


if __name__ == '__main__':
    data = create_data(10)
    print(data)
    print(merge_sort(data))
