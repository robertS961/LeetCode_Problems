'''

Intuition

My first thought was to change this tree into a graph with bidirectional edges and use a shorted path algorithm like Dijkstras.
I realized this would be a tad diffcult to keep track of which nodes from the current where left, right, and parent. So I decided to keep the TreeNode data structure and add a self.parent element to it. This way I can traverse all around the tree like it was a graph.
Now I will use dfs to traverse to every node in the graph and add the self.parent. I will also create a self.start variable to capture the starting node in memory.
Now I will use a shortest path Algo to traverse the graph. I won't use Dijkstras since the edges aren't weighted. Every edge has the same weight of 1 so a normal BFS will work wonders.
I use that start node variable to as my starting point in my queue.
I will iterate til I find the end node value, and keep track of the path along the way by adding the letter of the last direction I went.
I will return this path once I discover the end node as it will be the shortest path.

Space - O(n) to hold all n nodes in the seen set()
Time - O(n) since we have to traverse h (hieght) of the tree at most twice then replicate its path(to create a new string). (This might be n^2, unsure with the string replication)

'''

# CODE
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.start = None
        def dfs(curr, parent):
            curr.parent = parent
            if curr.val == startValue: self.start = curr
            if curr.left: dfs(curr.left, curr)
            if curr.right: dfs(curr.right, curr)

        dfs(root, None)
        q, seen = deque([(self.start, "")]), set([startValue])
        while q:
            for i in range(len(q)):
                node, path = q.pop()
                seen.add(node.val)
                if node.val == destValue: return path
                if node.left and node.left.val not in seen: q.appendleft((node.left, path + 'L'))
                if node.right and node.right.val not in seen: q.appendleft((node.right, path + 'R'))
                if node.parent and node.parent.val not in seen: q.appendleft((node.parent, path + 'U'))