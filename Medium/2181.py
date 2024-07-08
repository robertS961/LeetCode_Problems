'''
Intuition
1)We want two pointers. The first called left at the location of the first 0 and the other called right at the location of the second 0.
2)We want the right pointer to iterate to the second 0 and count all the values between them.
3)Change the value of the second 0 to the value of the accumulated total.
4)Now move the left pointer to the location of the right pointer(since we need to discard all those nodes between).
5)Move the right pointer up one space(since we don't want to add this total to the next bounded zeros total).
6)Continue this til the right pointer is at the end of the linked list.
7)Return the head of the linked list. We use a fake head so we return fakeHead.next. We do this to prevent any issues with deleting the head of the linked list since it will always be 0.

Space is O(1) since we are modifying the linked list in place
Time is O(n) since we need to visit each node in the linked list.

'''

#CODE


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode()
        left, right, tot = fakeHead, head.next, 0
        while right:
            while right.val != 0:
                tot += right.val
                right = right.next
            right.val = tot
            tot = 0
            left.next = right
            left = right
            right = right.next
        return fakeHead.next