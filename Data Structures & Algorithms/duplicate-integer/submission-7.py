class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # 1a. Brute force:
        # - Iterate through the array and for each element:
        #   - Iterate through the rest of the elements and for each 
        #     pair (Parent element and current child element):
        #     - Check whether both are equal and if equal, then return 
        #       true, otherwise continue
        # - If for loop finishes, then return False
        #
        # 1b. Complexity Analysis:
        # - Time = O(n^2) even in ideal cases
        # - Space = O(1) even in ideal cases
        #  
        # 1c. Implementation:
        # - Skipped

        # 2a. Optimized Approach:
        # - A hash set called uniqueNums = ()
        #   - A data structure that stores a collection of unique 
        #     elements in no particular order, using a hash table 
        #     to organize data internally
        #   - Traits: No Duplicates, Unordered sequence, It uses a hash
        #     function to convert each element into a hash code, which 
        #     maps the item to a specific "bucket" in memory. This allows 
        #     the program to jump straight to the item's location rather 
        #     than scanning the whole collection.
        # - Iterate through the array nums and for each number:
        #   - If the num is not in uniqueNums, then add it
        #   - If the num is in uniqueNums, then return True
        # - Return False if a full pass of the array finishes
        # 
        # 2b. Complexity:
        # - Time = O(n) because one iteration through the array and each
        #   time the check is mad as to whether the current element exists
        #   within the set, that check is also O(1) and overall, we do x n
        # - Space = O(n) because the biggest the set can be is if all numbers
        #   within nums are unique
        #
        # 2c. Implementation:
        # - Done below:

        # uniqueNums = {}
        uniqueNums = set()
        for num in nums:
            if num not in uniqueNums:
                uniqueNums.add(num)
            else:
                return True
        return False
