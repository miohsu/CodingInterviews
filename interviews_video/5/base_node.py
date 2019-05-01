class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def print_list_node(head):
    cur = head
    while cur != None:
        print(cur.val, end='->')
        cur = cur.next
    print()


def create_list_node(lst):
    """

    :param lst: List(int)
    :return: head Node
    """
    head = Node()
    cur = head
    for i in lst:
        node = Node(i)
        cur.next = node
        cur = cur.next
    return head