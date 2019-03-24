lst = [2, 3, 5, 4, 3, 2, 6, 7]


def duplicate(lst):
    if not lst or type(lst) != list:
        return False

    length = len(lst)
    for i in lst:
        if i < 1 or i >= length:
            return False

    start = 1
    end = length - 1
    while start <= end:
        mid = (start + end) // 2
        count = count_range(start, mid, lst)
        if start == end:
            if count > 1:
                return start
            else:
                break
        if count > (mid - start + 1):
            end = mid
        else:
            start = mid + 1


def count_range(start, end, lst):
    if not lst:
        return 0
    count = 0
    for i in lst:
        if start <= i <= end:
            count += 1
    return count


if __name__ == '__main__':
    print(duplicate(lst))
