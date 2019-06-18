"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""
from base_node import *


class Solution:
    def swapPairs(self, head):
        """

        :param head: ListNode
        :return: ListNode
        """
        dummyhead = Node()
        dummyhead.next = head
        cur = head
        pre = dummyhead
        while cur != None and cur.next != None:
            next = cur.next
            cur.next = next.next
            next.next = cur
            pre.next = next
            pre = cur
            cur = cur.next
        return dummyhead


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    link = create_list_node(data)
    print_list_node(link)
    sol = Solution()
    link = sol.swapPairs(link.next)
    print_list_node(link)
