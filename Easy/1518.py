'''

Intuition

1)First we want to drink all the full bottles and add them to our total.
2)Next we want to our empty bottles call them leftovers and add them to our newly drank leftovers. See how many full bottles we can get from turning these leftovers in. This is our new full total.
Note!! - We need to keep track of left overs from consecutive iterations since one iteration they can be non used then in the next they can still be used.
3)Do this until our number of full bottles + leftover is less than the exchange rate(Must stop here as we can't make any more full bottles than we have). This means we need to return our total and whatever full bottles we haven't drank yet.

Space O(1) - created two constant space variables
Time OLog(numExchange) - divide by the numExchange everytime.

'''

# CODE

class Solution:
    def numWaterBottles(self, fullBottles: int, numExchange: int) -> int:
        tot, leftover = 0,0
        while fullBottles + leftover >= numExchange:
            tot += fullBottles
            fullBottles, leftover = (fullBottles + leftover) // numExchange, (fullBottles + leftover) % numExchange
        return tot + fullBottles