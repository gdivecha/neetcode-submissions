class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 1a. Brute Force Approach:
        # - Iterate through each num within nums and for each num and its index:
        #   - Iterate through the rest of the elements on the right of the current num:
        #     - If parent num + current num = target
        #       - Return [lower num's index, higher num's index]
        #
        # 1b. Complexity:
        # - Time = O(n!) worst case because for each num, we iterate 
        #   (len(nums) - current num) times
        # - Space = O(1) because the checks are done in place
        # 
        # 1c. Implementation:
        # - Done below:
        # n = len(nums)
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]

        # 2a. Optimized Approach:
        # - Create a dict called remainderIndexMap = {}
        # - Iterate through the array nums and for each num and its index:
        #   - Check whether num exists within the remainderIndexMap keys:
        #     - If it doesn't exist:
        #       - remainder = target - num
        #       - Add to remainderIndexMap, remainder as key and current index as value
        #     - If it does exist:
        #       - Retrieve the value (index) of the key you just checked
        #       - Return [lower of current index or value, higher of current index or value]
        #
        # 2b. Complexity:
        # - Time = O(n) worst case since we do 1 single pass of the array
        # - Space = O(n) worst case since the biggest the dict can be is one key value pair
        #   per num in nums in a scenario where no 2 numbers in a pair == target
        #   although that is explicitly said won't happen so we resort to the worst
        #   case finding the second number as the last index
        #
        # 2c. Implementation:
        # - Done below:

        remainderIndexMap = {}
        for index,num in enumerate(nums):
            if num not in remainderIndexMap:
                remainderIndexMap[target - num] = index
            else:
                otherIndex = remainderIndexMap.get(num)
                return [min(otherIndex,index), max(otherIndex,index)]

        # Corrections by Claude:
        # - It’s O(n²), not O(n!). The inner loop runs (n-1) + (n-2) + ... + 1 times, 
        #   which is n(n-1)/2, and that’s O(n²). Factorial would mean trying every 
        #   ordering of the array.
        # - You don’t need min/max. The stored index always comes from an earlier 
        #   position than the current one, so otherIndex < index is guaranteed. 
        #   return [otherIndex, index] is enough.
        # - .get(num) can just be remainderIndexMap[num]. You already know the key exists.
        # - The version most people write stores value → index and checks whether 
        #   target - num is in the map. Yours is the mirror image and works fine, 
        #   but flipping it is easier to explain out loud: “for each number, have I 
        #   already seen the number that completes it?”
