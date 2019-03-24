lst = [2, 3, 1, 0, 2, 5, 3]


def duplicate_hash(lst):
    assert lst
    assert type(lst) == list
    lst_dict = dict()
    for i in lst:
        assert i < len(lst)
        if i in lst_dict:
            lst_dict[i] += 1
        else:
            lst_dict[i] = 1
    return lst_dict


def duplicate_o1(lst):
    assert lst
    assert type(lst) == list
    length = len(lst)
    for i in lst:
        if i < 0 or i >= length:
            return False
    index = 0
    while index < length:
        if index == lst[index]:
            index += 1
        else:
            if lst[index] == lst[lst[index]]:
                return True
            else:
                value = lst[index]
                lst[index], lst[value] = lst[value], lst[index]
    return False


if __name__ == '__main__':
    # print(duplicate_hash(lst))
    print(duplicate_o1(lst))
