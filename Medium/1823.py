'''
Intuition

Imported SortedList from sortedcontainers
Using the sortedlist we can remove elements in O(log(n)) time.
Create a sortedList with all the elments of 1-n.
Start at curr = 0 (0th element). Add k-1 to it since we are starting the k count at curr, we subtract 1.
Remove the element at that position in the list. If we remove the last indexed element then curr = 0. If we remove any other element the curr idx just takes the idx of the removed element.
Do this until 1 element is left. Return that element + 1 since I indexed everything starting at 0.

Space O(n) - filling a list with n numbers
Time O(nlog(n)) - n iterations and each iteration we remove an element in log(n) time

'''
 # CODE

from sortedcontainers import SortedList
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        sl = SortedList([i for i in range(n)])
        curr = 0
        while len(sl) > 1:
            removed = (curr + (k -1)) % len(sl)
            sl.remove(sl[removed])
            curr = 0 if removed == len(sl) else removed
        return sl[0] + 1
