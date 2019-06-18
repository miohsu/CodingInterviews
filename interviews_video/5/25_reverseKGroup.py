"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
from base_node import *


class Solution:
    def reverseKGroup(self, head, k):
        """

        :param head: ListNode
        :param k: int
        :return: ListNode
        """
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                node = head.next
                head.next = cur
                cur = head
                head = node
                count -= 1
            head = cur
        return head


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    link = create_list_node(data)
    print_list_node(link)
    sol = Solution()
    link = sol.reverseKGroup(link.next, 3)
    print_list_node(link)
