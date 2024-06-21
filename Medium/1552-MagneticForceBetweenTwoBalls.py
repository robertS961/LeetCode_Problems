class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        pos = sorted(position)

        def dis(force: int) -> bool:
            ans, curr = 1, pos[0]
            for i in range(1, n):
                if pos[i] -  curr >= force:
                    ans += 1
                    curr = pos[i]
            return ans >= m

        l,r = 0, pos[-1] - pos[0]
        while l < r:
            mid = r - (r- l) // 2
            if dis(mid):
                l = mid
            else:
                r = mid - 1
        return l
