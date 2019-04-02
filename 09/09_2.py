"""
    两个队列实现一个栈
"""


class MyQueue(object):
    def __init__(self, capacity=100):
        self._data = []
        self._capacity = capacity
        self._size = 0

    def put(self, value):
        if self._size < self._capacity:
            self._data.append(value)
            self._size += 1
        else:
            raise NameError('queue is full')

    def get(self):
        if self._data:
            self._size -= 1
            return self._data.pop(0)
        else:
            raise NameError('queue is empty')

    def __len__(self):
        return self._size


class MyStack(object):
    def __init__(self):
        self._q1 = MyQueue()
        self._q2 = MyQueue()

    def append_tail(self, value):
        if self._q2:
            self._q2.put(value)
        else:
            self._q1.put(value)

    def delete_tail(self):
        if not self._q1 and not self._q2:
            raise NameError('stack is empty')
        if self._q1:
            return self._re_storge(self._q1, self._q2)
        elif self._q2:
            return self._re_storge(self._q2, self._q1)

    def _re_storge(self, now, empty):
        while len(now) > 1:
            empty.put(now.get())
        return now.get()


if __name__ == '__main__':
    ms = MyStack()
    ms.append_tail(1)
    ms.append_tail(2)
    ms.append_tail(3)
    ms.append_tail(4)
    ms.delete_tail()
    ms.delete_tail()
    ms.delete_tail()
    pass
