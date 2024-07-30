class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt_b = 0
        dp = [0]
        for c in s:
            if c == 'b':
                cnt_b+=1
                dp.append( dp[-1] )
            else:
                dp.append( min(cnt_b,dp[-1]+1) )
        return dp[-1]