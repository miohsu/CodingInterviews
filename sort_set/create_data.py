from random import randint


def create_data(count):
    assert count > 0
    lst = []
    for i in range(count):
        lst.append(randint(0, 100))
    return lst
