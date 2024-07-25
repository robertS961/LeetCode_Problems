'''

Intuition

The problem becomes non trivial when they take away our built in sort function and want us to do it O(nlog(n))
The best way to perform this is merge sort!
We want to break down the array in a binary search fashion. We use a left and right point to find the middle. We then split the array in half, (left, middle) and (middle + 1, right). This way every element in the array is covered.
Next we send each half back into the function, until we end up with left == right. This means we are at one element. So we return this element in a list.
We will now will merge the list from the (left, middle) function call, and the (middle + 1, right) function call.
Since each list returned is sorted(only one element in each list at the first recursive return). We just take the smallest element off the front of each. This is guarenteed to be the absolute smallest item. We continue this one by using two pointers, one per array(assuming the lists have grown past 1 element now). Once one of the pointers reaches the end of the list, we exit this loop.
Now there is still elements in the array that has not been fully iterated. So we need to add those to the end of our built list.
Return the sorted list(Sorry been using the word array, it is a list).

Space - O(n) since we are creating a list of n elements

Time - O(nlog(n)) since we are iterating through a list of n elements on the last iteration of recursion. Then we are doing log(n) recursive steps since we are always dividing the array in half!

'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(left, right):
            if left == right: return [nums[left]]
            middle = (left + right)// 2
            l = sort(left, middle)
            r = sort(middle + 1, right)
            ans,i,j = [],0,0
            while i < len(l) and j < len(r):
                ans.append(min(l[i],r[j]))
                i_incr= l[i] <= r[j]
                i += i_incr
                j += not i_incr
            ans += l[i:] if i < len(l) else r[j:]
            return ans
        return sort(0, len(nums)- 1)