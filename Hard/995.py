'''
O(n) space and time
1)We keep track of an array cng(Short for changed). Everytime we change a bit we mark a 1, if we don't change then it stays at 0(every element is initalized to 0)
2)We also keep track of a current(Curr) and total(tot) changed bits. Everytime we need to change a bit, tot gets increased by 1 along with curr
3)Once we are further than k elements out, we need to refer to k elements back and see if we changed that bit. If we did then we need to decrease curr by 1.
4)For the element at nums[i] we need to see how many changes we have made. If it is an even change then the current bit stays the same if it is odd then the curr bit is flipped.
5)Using 4 with nums[i] we can see if the new current bit is a 0 or 1. If it is a 0 then we need to increase curr and tot by 1 and make cng[i] = 1.
6)Once we reach the last k - 1 bits, we can't make anymore changes. So using the above technique we see if the bits are all 1's. If anyone of them are a 0 we return -1
7)If we make it through all the above bits then we return the tot
'''


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        tot = curr = 0
        cng = [0] * len(nums)

        for i in range(len(nums) - k + 1):
            curr -= cng[i - k]
            if curr % 2 == 0 and nums[i] == 0:
                curr += 1
                tot += 1
                cng[i] = 1
            elif curr % 2 == 1 and nums[i] == 1:
                curr += 1
                tot += 1
                cng[i] = 1

        for i in range(len(nums) - k + 1, len(nums)):
            curr -= cng[i - k]
            if curr % 2 == 0 and nums[i] == 0:
                return - 1
            elif curr % 2 == 1 and nums[i] == 1:
                return -1
        return tot


class Solution2:
    def minKBitFlips2(self, nums: List[int], k: int) -> int:
        tot = curr = 0

        for i in range(len(nums) ):
            curr = curr - nums[i - k] if i >= k else curr - 0
            if i >= len(nums) - k + 1 and curr % 2 ^ nums[i] == 0: return -1
            if curr % 2 ^ nums[i] == 0: curr, tot, nums[i]  = curr + 1, tot + 1, 1
            else: nums[i] = 0
        return tot