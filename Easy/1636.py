'''

Intuition

I want to use a Counter() to keep track of the count of each number in nums.
I wanted to make a list from this counter with a tuple at each element in the list. The tuple will contain the count, number. Now I will sort based off the count of each item. When they are ties though, I want the larger number to go first.
I implemented the sorted() with the Counter from step 1) to achieve step 2). I then used a custom lambda function to sort based off the first parameter increasing and a "-" sign infront of the second parameter(so it will sort this one decreasing). This negative makes you take the largest first since the largerest positive number now becomes the largest negative number. Thus the smallest.
Then I wanted to assemble from this list the return list. All I had to do was take the count and the number from each spot in the list. Then duplicate that number equal to the count. Do this for every number in the list then return it.

Space - O(n) since I am creating a freq array with n elements of len(num)

Time - O(nlog(n)) since I have to go through n elements to sort the list and each sorting takes O(log(n)). Thus O(nlog(n))

'''

# CODE

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = sorted([(cnt, item) for item, cnt in Counter(nums).items()], key = lambda x: (x[0], -x[1]))
        return [item for cnt, item in freq for _ in range(cnt)]