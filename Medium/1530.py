'''

Intuition

1)Turn the tree into a graph by changing each node.left and node.right into an edge in a graph. When we reach a leaf node add it to our leafs set. (We need to store the actual node, where it is stored in memory. We can't store its value since each value is not unique)
2)Perform DFS on the binary tree to do the above transformation.
3)Now we have a set of leafs and a graph. So we will go from each leaf to the rest of the graph. We won't add nodes to the queue that we have visited before or have a larger distance than our max distance.
4)If we encounter another leaf node within the above constraints then we will check if we have this pair in our leaf_pairs. Leaf_pairs is just a set of all the pairs we have calculated as good pairs. If it is not in there then we increase our ans by 1.
5)Once we have done this for all our leaf nodes then we return ans.

Space - O(n) since we have n nodes in our dictionary.

Time - O(n^2) since we have n leaf nodes and for each leaf node we must traverse the n nodes graph.

'''

# CODE


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph, leafs = defaultdict(list), set()
        ans, seen_pairs = 0, set()

        def dfs(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)
            if not node.left and not node.right: leafs.add(node)

        dfs(root)

        for node in list(leafs):
            q, seen = deque([(node, 0)]), set([node])
            while q:
                curr, dist = q.popleft()
                for nei in graph[curr]:
                    if nei not in seen and nei in leafs and (
                    node, nei) not in seen_pairs and dist < distance and dist > 0:
                        ans += 1
                        seen_pairs.add((node, nei))
                        seen_pairs.add((nei, node))
                    if nei not in seen and dist + 1 <= distance:
                        q.append((nei, dist + 1))
                        seen.add(nei)
        return ans
