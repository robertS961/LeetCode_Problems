class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(sqrt(c) + 1)):
            b = sqrt(c - pow(a,2))
            if b == int(b): return True
        return False
