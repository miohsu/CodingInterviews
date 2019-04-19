"""
    三路快排
"""
import random


def quick_sort(nums, left, right):
    if right - left < 2:
        return nums
    r_index = random.randint(left, right - 1)
    nums[left], nums[r_index] = nums[r_index], nums[left]
    flag = nums[left]
    lt, gt = left, right  # [left, lt] < flag  [gt, right) > flag
    i = left + 1
    while i < gt:
        if nums[i] < flag:
            lt += 1
            nums[lt], nums[i] = nums[i], nums[lt]
            i += 1
        elif nums[i] > flag:
            gt -= 1
            nums[gt], nums[i] = nums[i], nums[gt]
        else:
            i += 1
    nums[left], nums[lt] = nums[lt], nums[left]
    quick_sort(nums, left, lt)
    quick_sort(nums, gt, right)
    return nums


def create_list(count):
    data = []
    for i in range(count):
        data.append(random.randint(0, 2))
    return data


if __name__ == '__main__':
    data = create_list(20)
    res = quick_sort(data, 0, 20)
    print(res)
