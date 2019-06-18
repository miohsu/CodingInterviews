"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
from base_node import print_list_node, create_list_node, Node


class Solution:
    def reverseBetween(self, head, m, n):
        """

        :param head: ListNode
        :param m: int
        :param n: int
        :return: ListNode
        """
        dummyhead = Node()
        dummyhead.next = head
        cur = head
        index = 1
        pre = dummyhead
        while index <= n:
            if index >= m:
                """todo"""
                if index == m:
                    m_node = cur
                    m_pre = pre
                if index == n:
                    n_node = cur
                    n_next = cur.next
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
                index += 1
            else:
                pre = cur
                cur = cur.next
                index += 1
        m_pre.next = n_node
        m_node.next = n_next
        return dummyhead


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    lst = [5]
    head = create_list_node(lst)
    print_list_node(head)
    sol = Solution()
    head = sol.reverseBetween(head.next, 1, 1)
    print()
    print_list_node(head)
