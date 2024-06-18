class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        w, ans,s_idx = sorted(worker), 0, len(worker)
        dp = sorted([(p,d) for p,d in zip(profit, difficulty)], key = lambda x: (-x[0],x[1]))

        for p,d in dp:
            idx  = bisect_left(w, d)
            ans += (s_idx - idx) * p if idx< s_idx else 0
            s_idx = idx if idx < s_idx else s_idx
        return ans    
