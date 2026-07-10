class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # First approach:
        # - Create a dictionary called numScore and it will hold the following:
        #   - Key = a number from within the array nums (any int)
        #   - Value = the number of repetitions of this number in question
        # - Iterate through the entire array nums with a for loop
        #   - In each iteration:
        #     - If the number does not exist in the dictionary:
        #       - Then, we add the number to the keys in the dictionary
        #         and we give that key a value of 1
        #     - If the number does exist in the dictionary:
        #       - Then, return true
        # - Return false if the runtime made it to the end of this program past the for loop
        numScore = {}
        for num in nums:
            print(numScore)
            if (num not in numScore.keys()):
                numScore[num] = 1
            else:
                return True
        return False