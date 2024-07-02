'''
Intuition
1)We want to take a Counter of both nums1 and nums2.
2)We want the intersection of these two counters so anything that overlaps. We Counter(nums1) & Counter(nums2) to get the intersection
3)With our new counter, we create a list of each number in 2) with its occurance equal to its count.
4)Return the list in 3)
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [num for num ,cnt in (Counter(nums1) & Counter(nums2)).items() for i in range(cnt)]