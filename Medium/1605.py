'''

Intuition

We want to build a grid based off row and column summation restraints.
Luckily the summation property is transative. So we can play around with the placement of each number without any worry and we know it is possible since the restraints of the problem are sum(rowSum) == sum(colSum)
How I came up with a solution was first creating a grid of all zeros. Then I want to fill in this grid starting from the top left to the bottom right with the correct answer.
We can do this with a double for loop. The first for loop will iterate through the rows and the second through the columns.
We will drop off numbers at each grid space based off the column til our row total is 0.
We will do this for each row til all the rows and column totals are fulfilled.
We will keep a prefix sum array of cols, which just keep tracks of the total of each column. This way we don't have to iterate through the grid each time to know the total of the column we are in.
Return the filled in grid at the end of the iterations.

Space O(mn) since we created a grid of length m rows by n columns

Time O(mn) since we are iterating through m rows and n columns to fill in the grid
'''

# CODE

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        grid = [[0] * len(colSum) for _ in range(len(rowSum))]
        cols = [0] * len(colSum)

        for i in range(len(rowSum)):
            curr = rowSum[i]
            for j in range(len(colSum)):
                if cols[j] < colSum[j]:
                    diff = colSum[j] - cols[j]
                    if curr > diff:
                        curr -= diff
                        grid[i][j] += diff
                        cols[j] += diff
                    else: # diff >= curr
                        grid[i][j] += curr
                        cols[j] += curr
                        break
        return grid