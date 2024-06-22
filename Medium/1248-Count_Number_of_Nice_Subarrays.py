class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count(n: list[int], odd:int) -> int:
            left = res = right = 0
            while right < len(n):
                odd -= n[right] % 2
                while odd < 0:
                    odd += n[left] % 2
                    left += 1
                res += right - left + 1
                right += 1
            return res
        return count(nums, k) - count(nums, k -1)
