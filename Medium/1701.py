'''

Intuition

1)We want to keep track of the finish time of each order. We call this curr.
2)We want to subtract the curr time from the start of the order to know how long the person waited.
3)We will accumulate wait throughout the loop. So add the wait time to the variable wait for every person in customers
4)At the end we will return the divided wait by the number of people(easily find this by taking the length of customers)

Space - O(1) since there is 2 constant space variables
Time - O(n) since we must iterate through the customer array

'''

#CODE

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait, curr = 0, customers[0][0]
        for (start,end) in customers:
            if start> curr: curr = start
            curr += end
            wait += (curr - start)
        return wait / len(customers)