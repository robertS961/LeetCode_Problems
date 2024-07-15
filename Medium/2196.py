'''

Intuition

1)We want to create a binary tree from a list of edges.
2)We need to keep track of each node in memory so we can refrence it. We can do this with a dictionary since each node has a unique value.
3)We also need to keep track of all the children nodes and parents. This way we can discover the root at the end of the problem. The root will be a parent that has never been a child.
4)Now we will iterate through the edges and construct the tree. First we always check if we have created the node for the parent or child. We do this by checking the dictionary. If we haven't then we create a new TreeNode.
5)Use a basic if statement to insert it to the left or right depending on the isleft val.
6)Iterate through all the edges then calculate the root by making a list of parent set - child set. This will give one value so use the list index of [0] to return this node from the dict.

Space - O(n) for n nodes since we keep storage of all n nodes
Time - O(max(e,n)) for e edges that we must iterate through and n nodes to iterate through to find the root.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(TreeNode)
        parents,kids = set(), set()
        for dad, kid, left in descriptions:
            parents.add(dad), kids.add(kid)
            dad = nodes[dad] if dad in nodes else TreeNode(val = dad)
            kid = nodes[kid] if kid in nodes else TreeNode(val = kid)
            if left: dad.left = kid
            else: dad.right = kid
            nodes[dad.val] = dad
            nodes[kid.val] = kid
        return nodes[list(parents - kids)[0]]