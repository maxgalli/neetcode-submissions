# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_to_list(self, tree_node, lst=None):
        if lst is None:
            lst = []
        if tree_node is None:
            return lst
        # (val, is_last, n_children)
        n_children = 0
        if tree_node.left:
            n_children += 1
        if tree_node.right:
            n_children += 1
        lst.append((tree_node.val, tree_node.left is None and tree_node.right is None, n_children))
        self.tree_to_list(tree_node.left, lst)
        self.tree_to_list(tree_node.right, lst)
        return lst

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_list = self.tree_to_list(root)
        print(root_list)
        sub_list = self.tree_to_list(subRoot)
        print(sub_list)
        # check if sublist
        n = len(sub_list)
        return any(root_list[i:i + n] == sub_list for i in range(len(root_list) - n + 1))