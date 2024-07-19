'''

Intuition

We want to find the max element of each column and the min element of each row.
To find the max element of each column we want to transpose each column into a row that we can iterate across. We do that with using the * to unpack the rows, then the zip() to take the elements from each unpakced object. Then put the maximums into a set since all the elements in the matrix are unique.
We will use sets again for the min of the rows. We will take the min of each row and put it into a set.

Now we want the intersection of the two sets as that element would be a min of a row and a max of a column. And return this as a list of elements or the null list.
Space - O(max(n,m)) for n max elements of the columns or m max elements of the rows.

Time - O(mn) must iterate through m rows and n columns to discover the max elements from each column and the min elements from each row.

'''

# CODE

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        maxCols = set(max(colT) for colT in zip(*matrix))
        minRows = set(min(row) for row in matrix)
        return maxCols & minRows  