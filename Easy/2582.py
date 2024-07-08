'''

Intuition

First find how many total passes(called totPasses) we are performing. We need this to find which way the pillow is being passed at the end of the time limit.
Second find the remainder of time at the occurance of the last pass. This will help us decide who has the pillow.
Now if the pillow is being passed left it means the totPasses % 2 == 0. So we are starting at person 1 for the remainder. Therefore return remainder + 1
If the pillow is being passed right then we can use an else statement since there is only two options(pass left or pass right). We will then return the n(1 indexed) - the remainder.
Space O(1) - 2 variables both O(1) space
Time O(1) - just need to compute division and mod

'''

# CODE

class Solution:
    def passThePillow(self, n, time):
        totPasses = time // (n- 1)
        remainder = time % (n-1)

        if not totPasses % 2: #Means we are going left to right
            return remainder + 1
        else: #Means we are going right to left
            return n - remainder       