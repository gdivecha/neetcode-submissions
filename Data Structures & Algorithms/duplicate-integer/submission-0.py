class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ##### Brute force Approach:
        # Pseudocode:
        # - For each element within the list:
        #   - First store the index of the current element in a variable
        #   - Iterate through the entire array one more time except for the current index:
        #     - If there is any value in the entire array that matches the value of the current index
        #       - Then, return true and break the loops
        # - If all values are iterated through, then that means that true was not returned and loops weren't broken, thrus return false
        # Complexity:
        # - Time complexity = O(n^2) because we have a nested for loop inside another for loop and worst case, we have no duplicates thus the
        #   the iterations occur pointlessly
        # - Space complexity = O(1) because we have not created any new dictionaries or any arrays or variable data structures to store anythign
        # Code:
        # for i, currentNum in enumerate(nums):
        #     for j, comparedNum in enumerate(nums):
        #         if((i!=j)and(currentNum==comparedNum)):
        #             return True
        # return False

        ##### Enhanced Approach #1:
        # Pseudocode:
        # - Create a dictionary (numberToAppearances) that holds the following:
        #   - Key = number that appears in the list
        #   - Value = how many times the number repeats itself in the list
        # - For each number element in the array:
        #   - If the number did not exist in the dictionary as a key, then:
        #     - Create a new dictionary entry like so -> numberToAppearances[num] = 1
        #   - Otherwise:
        #     - return True
        # - If all values are iterated through, then that means that true was not returned and loops weren't broken, thrus return false
        # Complexity:
        # - Time complexity = O(n) because we are going through the array once
        # - Space complexity = O(n) because if the array had all unique numbers, then the dictionary would be as big as the array
        # Code:
        numberToAppearances = {}
        for num in nums:
            appearances = numberToAppearances.get(num)
            if(not appearances):
                numberToAppearances[num] = 1
            else:
                return True
        return False
