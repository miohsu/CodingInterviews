"""
    归并排序
"""


def merge(lst, l, r, mid):
    data = lst.copy()
    i, j = l, mid
    k = l
    while i < mid and j < r:
        if data[i] < data[j]:
            lst[k] = data[i]
            i += 1
        else:
            lst[k] = data[j]
            j += 1
        k += 1
    while i < mid:
        lst[k] = data[i]
        i += 1
        k += 1
    while j < r:
        lst[k] = data[j]
        j += 1
        k += 1


def merge_sort_core(lst, l, r):
    if r - l <= 1:
        return
    mid = (r - l) // 2 + l
    merge_sort_core(lst, l, mid)
    merge_sort_core(lst, mid, r)
    merge(lst, l, r, mid)


def merge_sort(lst):
    l, r = 0, len(lst)
    merge_sort_core(lst, l, r)


if __name__ == '__main__':
    nums = [1, 43, 3, 532, 654, 9, 45]
    print(nums)
    merge_sort(nums)
    print(nums)
