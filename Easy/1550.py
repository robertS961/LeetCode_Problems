'''
Intuition
We want to iterate through arr and get 3 consecutive variables.
We can do that using zip with 3 different arrays starting at position 0,1,2
Check if each number is odd, if all are odd then add 1 to our list
Sum our list after the final iteration and if our sum is >= 1 we return True else False
'''

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return sum([a%2 == 1 and b%2 == 1 and c% 2 == 1 for a,b,c in zip(arr, arr[1:], arr[2:])]) >= 1