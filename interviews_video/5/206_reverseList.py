"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_node import Node, print_list_node, create_list_node


class Solution:
    def reverseList(self, head):
        """

        :param head: ListNode
        :return: ListNode
        """
        dummyhead = Node()
        dummyhead.next = head
        cur = dummyhead.next
        pre = None
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        dummyhead.next = pre
        return dummyhead


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    head = create_list_node(lst)
    print_list_node(head)
    sol = Solution()
    head = sol.reverseList(head.next)
    print()
    print_list_node(head)
