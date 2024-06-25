# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.tot = 0
        def findSum(node: TreeNode):
            if node.left: findSum(node.left)
            self.tot += node.val
            if node.right: findSum(node.right)
        def fixTree(node: TreeNode):
            if node.left: fixTree(node.left)
            node.val, self.tot = self.tot, self.tot - node.val
            if node.right: fixTree(node.right)

        if root: findSum(root)
        if root: fixTree(root)
        return root