'''

Intuition
1)First do an inorder DFS to get the numbers in sorted order. We know it is sorted order since the tree is a binary search tree and doing inorder will give you the nodes in increasing order.
2)Now we will use binary search on the array to create the best balancing act. This creates the best balancing act since binary search is log2. Thus this will balance the tree and guarantee a balanced tree.
3)We send in the indexes of 0 for left and length of the inorder array -1 for right. We do -1 since we don't want an index out of bounds error.
4)We constantly split the given left, right down the middle, m. We create a node with value based off the inorder array at index m. Then we discover the node.left and the node.right for the node by appyling the same process with new left and right values. The node.left tree will take on the same left val but its right val will be m-1 and the node.right will have the same right val but its left val will be m+1.
5)Use recursion on step 4 until every node has been seen
6)Return the newly created root node from the first recursion process

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []

        def dfs(root: TreeNode) -> None:
            if root.left: dfs(root.left)
            inorder.append(root.val)
            if root.right: dfs(root.right)

        def binarySearch(left: int, right: int) -> TreeNode:
            if left > right: return None
            m = (left + right) // 2
            node = TreeNode(inorder[m])
            node.left = binarySearch(left, m - 1)
            node.right = binarySearch(m + 1, right)
            return node

        dfs(root)
        return binarySearch(0, len(inorder) - 1)  