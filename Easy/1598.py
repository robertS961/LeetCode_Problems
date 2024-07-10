'''
Intuition

1)We want to keep track of the current depth of the folders.
2)We increase the depth when we route to a new folder. We don't increase the depth when we stay at the same folder. And we decrease the depth when we go to the parent.
3)I created a helper function to add 1, subtract 1, or add 0 based on step 2.
4)Iterate through the entire logs and call the helper function at each step.
Edge Case We need to make sure to watch out for being in the root directory and trying to go back one further. We can't go to negative 1. We solve this using max(0, ans + action). This way 0 is the lowest value we can ever go too.
5)Return the total depth

O(1) Space since we use 1 constant space variable ans
O(n) Time since we iterate through the log list of length n
'''

# CODE

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        def func(input):
            if input == "../":
                return -1
            elif input == "./":
                return 0
            return 1

        ans = 0
        for log in logs:
            action = func(log)
            ans = max(0, ans + action)
        return ans
