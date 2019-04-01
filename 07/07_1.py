"""
    输入一个二叉树的前序遍历和中序遍历的结果，请重建二叉树，假设输入的前序遍历和中序遍历的结果中不含重复的值。
    例如，输入前序遍历[1, 2, 4, 7, 3, 5, 6, 8]，中序遍历[4, 7, 2, 1, 5, 3, 8, 6]，则重建二叉树并输出它的头结点。
"""


class BinaryTreeNode(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def construct_core(preorder, inorder):
    root_node = BinaryTreeNode(preorder[0])
    if len(preorder) == 1:
        if len(inorder) == 1 and preorder == inorder:
            return root_node
        else:
            raise NameError('Error')
    index = 0
    length = len(inorder)
    while index < length and inorder[index] != root_node.value:
        index += 1
    if index >= length:
        raise NameError('Error')
    left_length = index
    right_length = length - index - 1
    if left_length > 0:
        root_node.left = construct_core(preorder[1:left_length + 1], inorder[0:left_length])
    if right_length > 0:
        root_node.right = construct_core(preorder[length - right_length:length],
                                         inorder[length - right_length:length])
    return root_node


def construct(preorder, inorder):
    if len(preorder) != len(inorder) or len(preorder) == 0:
        return None
    return construct_core(preorder, inorder)


def get_postorder(root):
    if root != None:
        get_postorder(root.left)
        get_postorder(root.right)
        print(root.value)


if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]

    # preorder = [1, 3, 4, 5]
    # inorder = [5, 4, 3, 1]
    root = construct(preorder, inorder)
    # print(root.value)
    get_postorder(root)
