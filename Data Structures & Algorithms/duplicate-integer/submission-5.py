class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # - Create a dictionary called numCounts
        # - This dictionary holds key value pairs as follows:
        #   - key = number within the nums array
        #   - value = repetitions of the number within the array
        # - Iterate through the array one by one and do the following:
        #   - If the current value is not in numCounts:
        #     - Add a dictionary key value pair with the number being
        #       the key and 1 being the count
        #   - Else if the current value is in numCounts:
        #     - return False
        # - If the for loop finishes completely through the array, then:
        #   - Return true

        # numCounts = {}
        # for num in nums:
        #     if num not in numCounts.keys():
        #         numCounts[num] = 1
        #         print(numCounts)
        #     else:
        #         return True
        # return False

        checkArray = []
        for num in nums:
            if num not in checkArray:
                checkArray.append(num)
        if len(checkArray)<len(nums):
            return True
        else:
            return False
