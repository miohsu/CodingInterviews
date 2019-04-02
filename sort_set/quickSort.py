"""
    快速排序
"""
import random


def quick_sort(array, left, right):
    if left >= right:
        return array
    flag = array[left]
    small = left
    big = right
    while small < big:
        while small < big and array[big] > flag:
            big -= 1
        array[small] = array[big]
        while small < big and array[small] <= flag:
            small += 1
        array[big] = array[small]
    array[small] = flag
    quick_sort(array, left, small - 1)
    quick_sort(array, small + 1, right)


def create_list(count):
    data = []
    for i in range(count):
        data.append(random.randint(0, 20))
    return data


if __name__ == '__main__':
    data = create_list(16)
    print(data)
    quick_sort(data, 0, len(data) - 1)
    print(data)
