
"""
75.Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = nums.count(0)
        white = nums.count(1) + red

        for i in range(len(nums)):
            if 0<=i< red: nums[i] = 0
            elif red<= i< white: nums[i] = 1
            else: nums[i] = 2
        return nums
