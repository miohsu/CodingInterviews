"""
    输入一个链表的头节点，从尾节点反过来打印这个链表。
"""
import random


class ListNode(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def create_list_node(head, length):
    current = head
    for i in range(length):
        tmp_node = ListNode(i)
        current.next = tmp_node
        current = current.next


def get_list_node(head):
    if not head.next:
        return
    current = head.next
    while current:
        yield current.value
        current = current.next


def get_reverse_list_node(head):
    if not head.next:
        return
    current = head.next
    get_reverse_list_node(current)
    print(current.value)


if __name__ == '__main__':
    head = ListNode()
    create_list_node(head, 10)
    gen = get_list_node(head)
    for i in gen:
        print(i)
    print('=' * 20)
    get_reverse_list_node(head)
