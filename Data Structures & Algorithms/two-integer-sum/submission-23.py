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

        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if (nums[i] + nums[j]) == target:
                    return [i,j]
