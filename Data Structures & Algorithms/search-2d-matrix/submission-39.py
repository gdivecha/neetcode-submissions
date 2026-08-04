class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # - Let's take a look at the criteria we are supposed to 
        #   work with:
        #   - You should aim for a solution with O(log(m * n)) time 
        #     and O(1) space, where m is the number of rows and n is 
        #     the number of columns in the matrix.
        #   - Binary Search Problem
        # - Let's take a look at the desired solution:
        #   - e.g. Input: matrix = [[ 1, 2, 4, 8],
        #                           [10,11,12,13],
        #                           [14,20,30,40]], 
        #                 ... and target = 40
        #     - We know that matrix is sorted in non-decreasing order
        #       - So, if we pick a number at random and that number in the
        #         row is lower than the target value, we must look at the
        #         right side of that number and if its the other way
        #         around, we need to look at the left of it
        #     - The first integer of every row is greater than 
        #       the last integer of the previous row
        #       - This means that if pick the first integer in any row at
        #         random and that value is lower than the target, similar 
        #         to the afore-mentioned column concept, we must look at
        #         at the rows following that row, otherwise, we look at
        #         the preceding rows
        #     - # of rows = m = 3
        #     - # of columns = n = 4
        #     - We treat this question like the basic binary search
        #       question we solved earlier in the list of binary search qs
        #     - @ rowBounds = [0,2]:
        #       - sampleRowSize = rowBounds[2] - rowBounds[0] + 1 = 3
        #       - middleRow = rowBounds[0] + sampleRowSize//2
        #                   = 0 + 1 = 1
        #       - middleRowRoot = matrix[1][0] = 10
        #       - 10 < 40:
        #         - is 40 between 10 and matrix[2][0] = 14?
        #           - No
        #           - So, we must figure out the new middle between the
        #             next row and the end of row numbers
        #           - rowBounds = [2,2]
        #     - @ rowBounds = [2,2]:
        #       - rowBounds[0] and rowBounds[1] are both 2
        #         - This means we are dealing with only 1 row
        #       - Is 40 between matrix[2][0] and matrix[2][3 or last col]?
        #         - Yes
        #         - So, we will do the following for the columns
        #     - @ colbounds = [0,3]:
        #       - sampleColSize = colbounds[1] - colbounds[0] + 1 = 4
        #       - middleCol = colbounds[0] + sampleColSize//2
        #                   = 0 + 2 = 2
        #       - middleColValue = matrix[2][2] = 30
        #       - 30 < 40:
        #         - We look at the right side of the row
        #         - colBounds = [3,3]
        #     - @ colbounds = [3,3]:
        #       - colbounds[0] and colbounds[1] are both 3
        #         - This means we are nailing down only 1 value instead of
        #           a sample size
        #       - Is matrix[2][3] == target?
        #         - Return True

        # Algorithm:
        # - sampleRowSize = len(matrix)
        # - sampleColSize = len(matrix[0])
        # - rowBounds = [0, sampleRowSize - 1]
        # - colBounds = [0, sampleColSize - 1]
        # - While rowBounds[0] <= rowBounds[1]:
        #   - sampleRowSize = rowBounds[1] - rowBounds[0] + 1
        #   - middleRow = rowBounds[0] + sampleRowSize//2
        #   - middleRowRoot = matrix[middleRow][0]
        #   - If rowBounds[0] == rowBounds[1]:
        #     - firstValue = matrix[rowBounds[0]][colBounds[0]]
        #     - finalValue = matrix[rowBounds[1]][colBounds[1]]
        #     - If firstValue <= target and target <= finalValue:
        #       - While colBounds[0] <= colBounds[1]:
        #         - sampleColSize = colbounds[1] - colbounds[0] + 1
        #         - middleCol = colbounds[0] + sampleColSize//2
        #         - middleColValue = matrix[middleRow][middleCol]
        #         - If middleColValue < target:
        #           - colbounds[0] = middleCol + 1
        #         - Else if middleColValue > target:
        #           - colbounds[1] = middleCol - 1
        #         - Else:
        #           - return True
        #     - Else:
        #       - return False
        #   - Else:
        #     - If middleRowRoot < target:
        #       - If target < matrix[middleRow + 1][0]:
        #         - rowBounds[1] = rowBounds[0]
        #       - Else:
        #         - rowBounds[0] = middleRow + 1
        #     - Else if middleRowRoot > target:
        #       - If target target > matrix[middleRow - 1][0]:
        #         - rowBounds[0] = rowBounds[1]
        #       - Else:
        #         - rowBounds[1] = middleRow - 1
        #     - Else:
        #       - return True
        # - return False

        sampleRowSize = len(matrix)
        sampleColSize = len(matrix[0])
        rowBounds = [0, sampleRowSize - 1]
        colBounds = [0, sampleColSize - 1]
        while rowBounds[0] <= rowBounds[1]:
            sampleRowSize = rowBounds[1] - rowBounds[0] + 1
            middleRow = rowBounds[0] + sampleRowSize//2
            middleRowRoot = matrix[middleRow][0]
            print(rowBounds)
            print("sampleRowSize", sampleRowSize)
            print("middleRow", middleRow)
            print("middleRowRoot", middleRowRoot)
            if rowBounds[0] == rowBounds[1]:
                firstValue = matrix[rowBounds[0]][colBounds[0]]
                finalValue = matrix[rowBounds[1]][colBounds[1]]
                if firstValue <= target and target <= finalValue:
                    while colBounds[0] <= colBounds[1]:
                        sampleColSize = colBounds[1] - colBounds[0] + 1
                        middleCol = colBounds[0] + sampleColSize//2
                        middleColValue = matrix[middleRow][middleCol]
                        if middleColValue < target:
                            colBounds[0] = middleCol + 1
                        elif middleColValue > target:
                            colBounds[1] = middleCol - 1
                        else:
                            return True
                else:
                    return False
            else:
                if middleRowRoot < target:
                    if middleRow + 1 < len(matrix) and target < matrix[middleRow + 1][0]:
                        rowBounds = [middleRow,middleRow]
                    else:
                        rowBounds[0] = middleRow + 1
                elif middleRowRoot > target:
                    if middleRow - 1 > -1 and target > matrix[middleRow - 1][0]:
                        rowBounds = [middleRow - 1, middleRow - 1]
                    else:
                        rowBounds[1] = middleRow - 1
                else:
                    return True
        return False





