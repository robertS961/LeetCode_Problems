'''
Two Solutions! O(n) and O(nlog(n))!!

Intuition for O(n(log(n)))
1)We want to find the city with the max number of roads attached to it. We want to make this the maximum value as it will us give the maximum total.
2)We will implement the start of topological sort and count edges going in and out from each road.
3)Then we will sort the values for each city in reverse. This way the city with the most roads is first.
4)Now we will go through the list and assign each value the maximum n value left. We will decrease our n by 1 each time since we can't assign the same value more than once.
5)Return the total.

Intuition for O(n)
1)Once you understand the above then you can consider not sorting. This would get rid of the O(log(n)) term.
2)We can get rid of sorting by storing the values in an array of values called srt. So if you have 4 roads then at srt[4] we will increase it by 1.
3)This way we can go through srt in decrasing order without sorting.
4)We will arrive at each number in srt and iterate through it until it is down to 0. You could do this faster with the summation formula(1 - n summation formula subtracted from 1- n - str[i] summation formula)
5)Iterate through all the indexes in srt and return the accumulated total

'''

# O(nlog(n)
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edgeCnt = defaultdict(int)
        ans = 0
        for u, v in roads:
            edgeCnt[u] += 1
            edgeCnt[v] += 1
        for i, val in enumerate(sorted(edgeCnt.values(), reverse=True)):
            ans += ((n - i) * val)
        return ans
# O(n)

class Solution2:
    def maximumImportance2(self, n:int, roads: list[list[int]]) -> int:
        ans, srt, ret = [0] * n, [0] * n, 0
        for src, dst in roads: ans[src], ans[dst] = ans[src] + 1, ans[dst] + 1
        for val in ans: srt[val] += 1
        for i in range(len(srt) - 1, 0, -1):
            while srt[i] >0:
                ret += (n * i)
                srt[i] -= 1
                n -= 1
        return ret