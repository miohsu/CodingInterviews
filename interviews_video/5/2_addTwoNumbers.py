"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
from base_node import *


class Solution:
    def addTwoNumbers(self, l1, l2):
        """

        :param l1:ListNode
        :param l2:ListNode
        :return:ListNode
        """
        count = 0
        head = Node()
        cur = head
        while l1 and l2:
            node = Node()
            count, sum = divmod(l1.val + l2.val + count, 10)
            node.val = sum
            cur.next = node
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            node = Node()
            count, sum = divmod(l1.val + count, 10)
            node.val = sum
            cur.next = node
            cur = cur.next
            l1 = l1.next
        while l2:
            node = Node()
            count, sum = divmod(l2.val + count, 10)
            node.val = sum
            cur.next = node
            cur = cur.next
            l2 = l2.next
        if count:
            node = Node(count)
            cur.next = node
        return head


if __name__ == '__main__':
    lst1 = [2, 4, 3]
    lst2 = [5, 6, 4]
    l1 = create_list_node(lst1)
    l2 = create_list_node(lst2)
    print_list_node(l1)
    print()
    print_list_node(l2)
    print()
    sol = Solution()
    head = sol.addTwoNumbers(l1.next, l2.next)
    print_list_node(head)
