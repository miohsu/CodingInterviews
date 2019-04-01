"""
    给定一个二叉树和其中一个节点，如何找出中序遍历序列的下个节点？树中的节点除了有两个分别指向左右子节点的指针，还有一个纸箱父节点的指针
"""


class BinaryTreeNode(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def init_node(node, left=None, right=None, parent=None):
    node.left = left
    node.right = right
    node.parent = parent


def create_binary_tree():
    node_dict = dict()
    for i in 'abcdefghi':
        node_dict[i] = BinaryTreeNode(i)
    init_node(node_dict['a'], node_dict['b'], node_dict['c'])
    init_node(node_dict['b'], node_dict['d'], node_dict['e'], node_dict['a'])
    init_node(node_dict['c'], node_dict['f'], node_dict['g'], node_dict['a'])
    init_node(node_dict['d'], parent=node_dict['b'])
    init_node(node_dict['e'], node_dict['h'], node_dict['i'], node_dict['b'])
    init_node(node_dict['f'], parent=node_dict['c'])
    init_node(node_dict['g'], parent=node_dict['c'])
    init_node(node_dict['h'], parent=node_dict['e'])
    init_node(node_dict['i'], parent=node_dict['e'])
    return node_dict


def find_next_inorder_node(node):
    if node == None:
        return
    next_node = None
    if node.right:
        right_node = node.right
        while right_node.left:
            right_node = right_node.left
        next_node = right_node

    elif node.parent:
        parent = node.parent
        if node == parent.left:
            next_node = parent
        elif node == parent.right:
            current = node
            while parent and current == parent.right:
                current = parent
                parent = parent.parent
            next_node = parent
    return next_node


if __name__ == '__main__':
    tree_dict = create_binary_tree()
    res = find_next_inorder_node(tree_dict['g'])
    if res:
        print(res.value)
    else:
        print('None')
