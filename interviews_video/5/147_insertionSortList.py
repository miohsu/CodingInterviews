"""
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。


示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""
from base_node import *


class Solution:
    def insertionSortList(self, head):
        """

        :param head: ListNode
        :return: ListNode
        """
        dummyhead = Node()
        dummyhead.next = head
        cur = head
        if cur == None or cur.next == None:
            return head
        count = 2
        pre = cur
        cur = cur.next
        while cur != None:
            if cur.val >= pre.val:
                pre = cur
                cur = cur.next
                count += 1
                continue
            next = cur.next
            pre.next = next
            num = 1
            inner_cur = dummyhead.next
            inner_pre = dummyhead
            while num < count:
                if inner_cur.val > cur.val:
                    inner_pre.next = cur
                    cur.next = inner_cur
                    break
                else:
                    inner_pre = inner_cur
                    inner_cur = inner_cur.next
                num += 1
            count += 1
            cur = next
        return dummyhead


if __name__ == '__main__':
    data = [4, 2, 3, 1]
    link = create_list_node(data)
    print_list_node(link)
    sol = Solution()
    link = sol.insertionSortList(link.next)
    print_list_node(link)
