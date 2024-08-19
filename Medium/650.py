# Intuition
1) We need to keep track of the total amount of letters we have pasted, along with the count of letters currently in our copy button.
2) We then have two options per step. We can copy the current letters, or paste what we have in our copy button.
3) Our base case will be when our total letters equals our desired total letters. Then we will return 0 steps.
4) However there are edge cases. First we need to make sure we don't paste when we have nothing copied. Second we need to make sure we don't copy if we already copied the same sequence before. Third we need to make sure we stop iterating if we create a greater number of 'A's then we need.
5) Now this is a solid backtracking solution that will run in $2^{n}$ time. We can increase this speed by using a cache aka dynamic programming. We know we can use dp since there will be several subproblems that reoccur.
6) Lastly we want to return the minimum number of operations at each subproblem based on the two decision in step 2.
7) Return the dp function which will contain the minimum.

Time O(n^2) since we have 2 variables in our dp. Total which max size is n along with copy which max size is also n
Space O(n^2) with the same explanation as time.

class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dp(tot, copy):
            if tot == n: return 0
            if tot > n: return inf
            ans = inf
            if copy != 0: ans = min(ans, 1 + dp(tot + copy, copy))
            if copy != tot: ans = min(ans, 1+ dp(tot, tot))
            return ans
        return dp(1, 0)
