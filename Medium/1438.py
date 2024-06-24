class Solution:
    def longestSubarray(self, A, limit):
        inc, dec = deque(), deque()
        ans, left =  0, -1
        for i, num in enumerate(A):
            while inc and num <= inc[-1][0]: inc.pop()
            while dec and num >= dec[-1][0]: dec.pop()
            inc.append((num, i))
            dec.append((num, i))
            while abs(dec[0][0] - inc[0][0]) > limit:
                if dec[0][1] < inc[0][1]: left = dec.popleft()[1]
                else: left = inc.popleft()[1]
            ans = max(ans, i - left)
        return ans



        
