"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
from base_node import *


class Solution:
    def removeElements(self, head, val):
        """

        :param head: ListNode
        :param val: int
        :return: ListNode
        """
        dummyhead = Node()
        dummyhead.next = head
        cur = head
        pre = dummyhead
        while cur != None:
            if cur.val == val:
                """todo"""
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummyhead


if __name__ == '__main__':
    lst = [1, 2, 6, 3, 4, 5, 6]
    head = create_list_node(lst)
    print_list_node(head)
    sol = Solution()
    head = sol.removeElements(head.next, 6)
    print_list_node(head)
