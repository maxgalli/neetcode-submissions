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
            lst.append(None)
        else:
            lst.append(tree_node.val)
            self.tree_to_list(tree_node.left, lst)
            self.tree_to_list(tree_node.right, lst)
        return lst

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.tree_to_list(p) == self.tree_to_list(q)