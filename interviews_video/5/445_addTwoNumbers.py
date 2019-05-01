"""
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。



你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7
"""
from base_node import *
from itertools import zip_longest


class Solution:
    def addTwoNumbers(self, l1, l2):
        """

        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        str1 = ""
        str2 = ""
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        sum = str(int(str1) + int(str2))
        cur = Node()
        head = cur
        for ch in sum:
            node = Node(int(ch))
            cur.next = node
            cur = cur.next
        return head

    def addTwoNumbers_2(self, l1, l2):
        lst1 = []
        lst2 = []
        while l1:
            lst1.append(l1.val)
            l1 = l1.next
        while l2:
            lst2.append(l2.val)
            l2 = l2.next
        count = 0
        head = Node()
        cur = head
        for x, y in zip_longest(reversed(lst1), reversed(lst2), fillvalue=0):
            count, sum = divmod(x + y + count, 10)
            node = Node(sum)
            cur.next = node
            cur = cur.next
        if count:
            node = Node(count)
            cur.next = node
        return self.reverseList(head)

    def reverseList(self, head):
        cur = head.next
        pre = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        head.next = pre
        return head


if __name__ == '__main__':
    l1 = create_list_node([7, 2, 4, 3])
    l2 = create_list_node([5, 6, 4])
    print_list_node(l1)
    print()
    print_list_node(l2)
    sol = Solution()
    # head = sol.addTwoNumbers(l1.next, l2.next)
    head = sol.addTwoNumbers_2(l1.next, l2.next)
    print()
    print_list_node(head)
