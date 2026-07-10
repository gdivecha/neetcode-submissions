class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # - The easiest checks for the board to be invalid are if either fo these 2 are violated:
        #   - Each row must contain the digits 1-9 without duplicates
        #   - Each column must contain the digits 1-9 without duplicates
        #   - E.g. Example 1 shown in the question:
        #     - @ Row 1 -> ["1","2",".",".","3",".",".",".","."] -> numFrequency = {1:1,2:1,3:1}
        #     - @ Row 2 -> ["4",".",".","5",".",".",".",".","."] -> numFrequency = {4:1,5:1}
        #       ... and so on -> If at any point, the frequency of a number reaches 2, that's whe
        #       it returns False right away
        #   - So we do this for each row and for each column
        # - Now, we must check for this condition: 
        #   - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates
        #   - Let's look only at:
        #     ["1","2","."]
        #     ["4",".","."]
        #     [".","9","8"]
        #   - We can look at each column at a time: (* Step)
        #     - @ col = 0:
        #       - numFrequency = set()
        #       - @ row = 0 -> 1 -> 1 not in numFrequency
        #       - @ row = 1 -> 4 -> 4 not in numFrequency
        #       - @ row = 2 -> . -> . not a number
        #       - numFrequency = {1,4}
        #     - @ col = 2:
        #       - numFrequency = set()
        #       - @ row = 0 -> 2 -> 2 not in numFrequency
        #       - @ row = 1 -> . -> . not a number
        #       - @ row = 2 -> 9 -> 9 not in numFrequency
        #       - numFrequency = {1,4,2,9}
        #     - @ col = 3:
        #       - numFrequency = set()
        #       - @ row = 0 -> . -> . not a number
        #       - @ row = 1 -> . -> . not a number
        #       - @ row = 2 -> 8 -> 8 not in numFrequency
        #       - numFrequency = {1,4,2,9,8}
        #   - We go to the next 3x3 box to the right of it
        #   - Also, keep i mind, that we do the * step for all 9 rows at the same time to save time
        #   - Logic is that even if even 1 number was in the numFrequency set upon the column row checks
        #     then we return False
        
        # Algorithm:
        # - Iterate through each row of the board and for each row:
        #   - Create an empty set called numFrequency that holds a list of unique numbers that exist in the row
        #   - Iterate through each column of the board and for each column:
        #     - If currentEntry not in numFrequency:
        #       - Then numFrequency.add(currentEntry):
        #     - Else:
        #       - Return False
        # - Iterate through each column of the board and for each column:
        #   - Create an empty set called numFrequency that holds a list of unique numbers that exist in the column
        #   - Iterate through each row of the board and for each row:
        #     - If currentEntry not in numFrequency:
        #       - Then numFrequency.add(currentEntry):
        #     - Else:
        #       - Return False
        # - row = 0
        # - column = 0
        # - numFrequencyBox = [set(),set(),set()]
        # - For each column in the board;
        #   - If column % 3 == 0, then numFrequencyBox = [set(),set(),set()]
        #   - For each row in the board:
        #     - corrspondingBox = (row+1)%3
        #     - If the value is a number and that number does not exist in numFrequencyBox[corrspondingBox]:
        #       - Add that number to numFrequencyBox[corrspondingBox]:
        #     - Else if the value is ".":
        #       - Continue
        #     - Else:
        #       - Return False
        # - Return True

        for row in range(len(board)):
            numFrequency = set()
            for column in range(len(board)):
                entry = board[row][column]
                if (entry.isdigit() and int(entry) not in numFrequency):
                    numFrequency.add(int(entry))
                elif entry.isdigit() and int(entry) in numFrequency:
                    return False
        for column in range(len(board)):
            numFrequency = set()
            for row in range(len(board)):
                entry = board[row][column]
                if (entry.isdigit() and int(entry) not in numFrequency):
                    numFrequency.add(int(entry))
                elif entry.isdigit() and int(entry) in numFrequency:
                    return False
        numFrequencyBox = [set(),set(),set()]
        for column in range(len(board)):
            if (column)%3==0:
                numFrequencyBox = [set(),set(),set()]
            for row in range(len(board)):
                correspondingBox = row//3
                entry = board[row][column]
                print(entry)
                if (entry.isdigit() and (int(entry) not in numFrequencyBox[correspondingBox])):
                    numFrequencyBox[correspondingBox].add(int(entry))
                elif (entry.isdigit() and (int(entry) in numFrequencyBox[correspondingBox])):
                    return False
        return True

        








