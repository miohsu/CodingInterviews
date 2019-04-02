"""
    用两个栈实现一个队列。队列的生命如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在尾部插入节点和在队列头部删除节点
"""


class MyStack(object):
    def __init__(self, capacity=100):
        self._data = []
        self._capacity = capacity
        self._size = 0

    def put(self, value):
        if self._size < self._capacity:
            self._data.append(value)
            self._size += 1

    def get(self):
        if self._data:
            self._size -= 1
            return self._data.pop()

    def __bool__(self):
        return bool(self._data)

    def __len__(self):
        return self._size

    def capacity(self):
        return self._capacity


class MyQueue(object):
    def __init__(self):
        self._s1 = MyStack()
        self._s2 = MyStack()

    def appendTail(self, value):
        self._s1.put(value)

    def deleteHead(self):
        if not self._s1 and not self._s2:
            raise EOFError
        if not self._s2:
            while self._s1:
                self._s2.put(self._s1.get())
        return self._s2.get()


if __name__ == '__main__':
    mq = MyQueue()
    mq.appendTail(1)
    mq.appendTail(2)
    mq.appendTail(3)
    mq.deleteHead()
    mq.deleteHead()
