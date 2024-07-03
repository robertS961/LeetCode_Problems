"""
Intuition
1)We can see there is 4 total options to spend our 3 points. All the options are written out in my code!
2)Take the min of the 4 options and return it

Follow up. What if there was N options? How do you solve this?
1)You should go through all n+1 choices and return the min.
2)You could do this with 2 pointers where you increase one by 1 and decrease the other by 1
3)Keep track of the overall min and compare it each time
4)Return the overall min
"""

class Solution:
    def minDifference(selfself, nums:list[int]) -> int:
        n = sorted(nums)
        l, r = 0, len(n) - 1
        return min(n[r] - n[l + 3], n[r - 1] - n[l + 2], n[r - 2] - n[l + 1], n[r - 3] - n[l]) if r >= 4 else 0