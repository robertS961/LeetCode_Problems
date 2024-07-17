'''

Intuition

At first I thought of going down the tree with a normal DFS. However, I couldn't come up with a way to traverse down and delete nodes(there is a way, check Lees and others posts)
So I decided to do a post order traverse that way the node wouldn't be effected by whats below it(hence post order) and we would start on the bottom rung and work our way up(hence a deletion would only be below it and wouldn't effect the path).
If the current node is in the delete set(turn it into a set so you can look values up in O(1) time, compared to O(n) for a list) then we want to add its left child and right child to our roots list(if they exist). Then return None to the node above since this path will now be destroyed by deleting this node.
We need to make sure we can update the left and right child of the curr since those paths will get ruptured if a node is deleted beneath them.
Eventually we will exit the dfs, we must check if we deleted the original root. If we didn't then we need to add that orginal root to our roots list. If we did then return the list as is.

Space - O(n) we created a roots list to return which could hold all the nodes and there are n nodes.

Time - O(n) we must go through all the nodes of the tree and check each one to see if it needs deleted. There are n nodes.
'''

# CODE

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        roots = []
        to_delete = set(to_delete)
        def dfs(node):
            if node.left: node.left = dfs(node.left)
            if node.right: node.right = dfs(node.right)
            if node.val in to_delete:
                if node.left: roots.append(node.left)
                if node.right: roots.append(node.right)
                return None
            return node
        dfs(root)
        return roots + [root] if root.val not in to_delete else roots