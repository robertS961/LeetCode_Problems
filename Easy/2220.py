#Solution 1
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start ^= goal
        ret = 0
        for i in range(32):
            ret += (1<<i & start) != 0
        return ret
#Solution 2
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
