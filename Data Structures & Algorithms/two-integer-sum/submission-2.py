class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # - Create a dictionary called remainderLocations
        # - This dictionary should hold the following:
        #   - Key = A number that exists within the nums array
        #   - Value = A number that represents an index within nums
        # - We loop through the array nums and for each nums:
        #   - We first calculate the difference (target - currentNum)
        #   - If that remainder doesn't exist inside remainderLocations:
        #     - Add the entry as:
        #       - Key = current number within nums
        #       - Value = current index
        #   - Otherwise if it does exist:
        #     - Return [value associated to that remainder key, index of the currentNum]

        remainderLocations = {}
        for index,num in enumerate(nums):
            desiredRemainder = target - num
            if desiredRemainder not in remainderLocations.keys():
                remainderLocations[num] = index
            else:
                return [remainderLocations.get(desiredRemainder), index]