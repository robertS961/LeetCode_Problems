'''
Intuition

Part 1

We want to find all the critical points and store them in a list.
To find a critical point we must know the prev, curr, and next. Luckily we already know the curr by using node.val, and the next by using node.next.val. So how to find previous? You could use a double linked list but that adds O(n) memory since every node would need a self.prev attribute. Instead lets store the prev val in a prev variable.
Now iterate through the entire linked list and check if it is a critical min or max point. Make sure to change prev to the curr value at the end of each loop and move the curr pointer.
We also need to keep track of an idx variable for the index we are currently at in the linked list. We need the idx to properly solve part 2.

Part 2

We need to find the max and min of our critical points indexes.
Finding the max is easy as we subtract the smallest critical point from the largest. Since we went through the linked list in order, it is in sorted order. So subtract the last element from the first.
To find min we want to check each neighboring pair. This would be the closest possible critical point 1 could be to critical point 2. There is no reason to check any other combination of point 1 with any other point.
We will use pairwise for this and discover the min of all the pairwise points.
We will return this min and max unless the len(points) <= 1. Meaning we could never find a pair for max or min. Then we return the base case [-1.-1]
'''

#CODE


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, curr, points, idx = head.val, head.next, [], 1
        while curr.next:
            if curr.val > prev and curr.val > curr.next.val:
                points += [idx]
            elif curr.val < prev and curr.val < curr.next.val:
                points += [idx]
            idx += 1
            prev = curr.val
            curr = curr.next
        return [-1, -1] if len(points) <= 1 else [min(b - a for a, b in pairwise(points)), points[-1] - points[0]]

