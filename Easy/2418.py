'''

Intuition

We want a list of the heights in descending order with the corresponding names
We will zip together height and names in a tuple then sort by the height in descending order
Return the name from each tuple pair of the sorted list. Put all these names into a list.

Space - O(n) creation of the sorted list

Time - (O(n)log(n)) since we must iterate through the entire list of n heights and sort it (log(n). Thus O(nlog(n)).

'''

# CODE

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_name = sorted([(h,n) for n,h in zip(names, heights)], key = lambda x: x[0], reverse = True)
        return [n for (h,n) in height_name]