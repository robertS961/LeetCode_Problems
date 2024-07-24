'''

Intuition

The first step is to map each number in nums to its new transformation using the list mapping.
We can do this by turning the number into a string so we can iterate over each digit in the number. We should also create a list to store the new digits for this numbers mapping.
Next we iterate over each char in the number(represented by a digit in character form). And turn it into an int so we can plug it into the mapping list. This will output the new digit(int val). We take that int and turn it into a string and append it to our a list.
Once we finish iterating over the number. We will use "".join to concat the list to a string then take the int of this string. This will get rid of the leading zeros and give us the correct value in int form.
We will do steps 2-4 for all the nums in num.
However when it comes to sorting the list we need to keep the same mapped values in orginal relative order. How to do that?
When we are iterating through each num in nums. We will store its orginal index value with its new mapping value. This way when we sort by the mapping value, if there is a tie we will sort by the orginal index value. Thus keeping the array sorted and keeping the relative order for ties.
Now we have a correctly sorted list of (mapped nums, orginalIdx). So we iterate through this and create a new list where each element is determined by the nums[orginalIdx], since they want the orginial numbers sorted, not the mapped numbers.
Return the list created in 8).

Space - O(n) since we are creating a list of all the mappings from nums. Nums is the size of len(nums) which we will call n.

Time - O(32n) ~ O(n) since need to iterate through each num in nums which is of length n. Then for each num we need to iterate through all its digits. It is bounded by 2
32. Hence O(32n).
'''

# CODE

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = []
        for i, num in enumerate(nums):
            new_num = []
            for char in str(num):
                r = mapping[int(char)]
                new_num.append(str(r))
            new_num = "".join(new_num)
            mapped.append((int(new_num), i))
        return [nums[idx] for num, idx in sorted(mapped, key = lambda x:(x[0], x[1]))]


