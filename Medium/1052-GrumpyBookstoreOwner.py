class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        window = 0
        bst = 0
        for i in range(len(customers)):
            window += customers[i] * (grumpy[i])
            if i + 1 >= minutes:
                bst= max(bst, window)
                window -= customers[i + 1 -minutes] *(grumpy[i+1 - minutes])
        return sum(num for i,num in enumerate(customers) if grumpy[i] == 0) + bst
