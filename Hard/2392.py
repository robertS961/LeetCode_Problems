'''

Intuition

This is a tough problem and I originally created two helper functions. One for the rows and one for columns. After looking at the solutions, I realized it can be done with 1.
The first step is to realize we need to build both the rows and cols in a certain order. Much like a directed graph. This hints us to use dfs or bfs.
Next we realize this graph needs to be built from the nodes that have no restrictions on them. They should go at the bottom since other nodes need to be above or to the right of them.
How do we find these nodes? Use topological sort. The nodes with 0 incoming edges can go anywhere.
Now bfs is easier to use with topological sort so I am going to use that.
As I use these nodes in my bfs I want to go to their Neighbor nodes, which I will use a pre-build graph for. When I arrive at neighbor nodes I want to see how many incoming edges they have. This makes sure that everything below them is already in list. If it isn't then I can use them yet. So I will take off one incoming edge. If there incoming edges equal 0 then I can add them to the queue.
I will continue this til my q is empty. However, how do I know if it is a valid partition of the elements?
The key is to think of our graph like a tree. Trees are great because you can never have a cycle unlike a graph. Same with this problem, as a cycle would make it impossible to solve. Thus if we had a cycle our bfs would never reach those nodes because they all would have a minimum of 1 incoming edge. And we start with all the nodes with 0 incoming edges.
Thus we check at the end if our list contains all the elements. If it does then we have a valid partition, if it doesn't then return an emepty list so we can return an empty grid.
Side note EDGE CASES: for nodes that don't have any edges connecting them will also need to be inserted. The second edge case is double edges. like 4 before 3, twice. We can easily fix this with making sure all the edges are unique with a set.
Now we will call the helper function for both rows and columns. IF either returns an empty set then we return an empty grid.
Lastly we will make a grid filled with zeros as that is the default. Then plug in the numbers based off their index in both the row and cols array.
Return the final array.
The largest constraint is actually the size of the R and C. We will call these R and C.

Space - O(max(R,C)) since we are making a set of the unique edges. This will be our largest space requirement. Whichever has more unique elements will be the space requirement.

Time - O(max(R,C)) since we have to iterate through both R and C whichever is longer in length will take the max time.

'''

# CODE

class Solution:
    def buildMatrix(self, k: int, R: List[List[int]], C: List[List[int]]) -> List[List[int]]:
        def arrange(A):
            graph, edges = defaultdict(set), defaultdict(int)
            srcDst, q, ans = set(), deque(), []
            for src, dst in A:
                if (src,dst) not in A: srcDst.add((src,dst))
            for src, dst in srcDst:
                graph[src].add(dst)
                edges[dst] += 1
            for i in range(1, k + 1):
                if edges[i] == 0 or i not in edges: q.append(i)
            while q:
                curr = q.popleft()
                ans.append(curr)
                for nei in graph[curr]:
                    edges[nei] -= 1
                    if edges[nei] == 0: q.append(nei)
            return ans if len(ans) == k else []

        ans1, ans2 = arrange(R), arrange(C)
        if not ans1 or not ans2: return []
        grid = [[0]* k for _ in range(k)]
        for i in range(1,k + 1):
            grid[ans1.index(i)][ans2.index(i)] = i
        return grid