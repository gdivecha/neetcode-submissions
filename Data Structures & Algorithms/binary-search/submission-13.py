class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # - Let's try to figure out the desired behavior based on 
        #   the following criteria:
        #   - You should aim for a solution with O(logn) time 
        #     and O(1) space, where n is the size of the input array.
        #   - Binary search problem
        # - Since we have the array already sorted in an ascending order,
        #   we must use the best ability of binary search to the maximum
        #   potential which works as follows:
        #   - On paper, if we want to find a target number in an array,
        #     we split the sample array by half and we check whether the
        #     element number we split the sample size is greater than
        #     or lower than the target.
        #     - If the number we split at is lower, then we look at the
        #       right side of the split sample and repeat the process
        #     - Otherwise, we look at the left side and repeat the process
        #   - Now, we can't use recursion even though it is really 
        #     appealing because doing recursion means to call the search
        #     method recursively with a sample of the original array as
        #     the parameter each time and according to how python works,
        #     calling a method in python and passing in a slice of an array
        #     also counts as making a new array and sending that over,
        #     meaning that despite the time complexity stays at O(logn),
        #     this soln. would still result in n/2 space waster each time 
        #     just trying to call the method alone and it would also result
        #     in O(logn) space complexity as well when what we really
        #     need is O(1) space comlexity.
        #   - So, we need to do everythign in-place and keep the space
        #     complexity at a bare minimum
        # - Desired Behavior:
        #   e.g. [-1,0,2,4,6,8,11,14,19,23,24] & target = 19
        #   - sampleBounds = [0,10]
        #   - while True:
        #     - @ sampleBounds = [0,10]:
        #       - sampleSize = sampleBounds[1] - sampleBounds[0] + 1 = 11
        #       - middleIndex = sampleBounds[0] + sampleSize//2 - 1 = 0+5-1 = 4
        #       - middleElement = 6
        #       - 6 < 19:
        #         - sampleBounds = [5,10]
        #     - @ sampleBounds = [5,10]:
        #       - sampleSize = sampleBounds[1] - sampleBounds[0] + 1 = 6
        #       - middleIndex = sampleBounds[0] + sampleSize//2 - 1 = 5+3-1 = 7
        #       - middleElement = 14
        #       - 14 < 19:
        #         - sampleBounds = [8,10]
        #     - @ sampleBounds = [8,10]:
        #       - sampleSize = sampleBounds[1] - sampleBounds[0] + 1 = 3
        #       - middleIndex = sampleBounds[0] + sampleSize//2 - 1 = 8+1-1 = 8
        #       - middleElement = 19
        #       - 19 == 19:
        #         - returns middleElement
        #       - Imagine now that target was 25 for demo purposes:
        #       - 19 < 25:
        #         - sampleBounds = [9,10]
        #     - @ sampleBounds = [9,10]:
        #       - sampleSize = sampleBounds[1] - sampleBounds[0] + 1 = 2
        #       - middleIndex = sampleBounds[0] + sampleSize//2 - 1 = 9+1-1 = 0
        #       - middleElement = 23
        #       - 23 < 25:
        #         - sampleBounds = [10,10]
        #     - @ sampleBounds = [10,10]:
        #       - sampleSize = sampleBounds[1] - sampleBounds[0] + 1 = 1
        #       - Since sampleSize == 1, we look at only the value at element 10
        #         - 23 is not 25, so we return false
        

        # Algorithm:
        # - sampleBounds = [0,len(nums)-1]
        # - while True:
        #   - sampleSize = sampleBounds[1] - sampleBounds[0] + 1
        #   - if sampleSize == 1:
        #     - if sampleBounds[0] != target:
        #       - return -1
        #     - else:
        #       - return sampleBounds[0]
        #   - else:
        #     - middleIndex = sampleBounds[0] + sampleSize//2 - 1
        #   - middleElement = nums[middleIndex]
        #   - if middleElement < target:
        #     - sampleBounds[0] = middleIndex + 1
        #   - Else if middleElement > target:
        #     - sampleBounds[1] = middleIndex - 1
        #   - Else:
        #     - return middleIndex

        sampleBounds = [0,len(nums)-1]
        if sampleBounds[0] == sampleBounds[1]:
            if nums[sampleBounds[0]] == target:
                return 0
            else:
                return -1
        else:
            while sampleBounds[1] >= sampleBounds[0]:
                print(sampleBounds)
                sampleSize = sampleBounds[1] - sampleBounds[0] + 1
                if sampleSize == 1:
                    if nums[sampleBounds[0]] != target:
                        return -1
                    else:
                        return sampleBounds[0]
                else:
                    middleIndex = sampleBounds[0] + sampleSize//2 - 1
                    middleElement = nums[middleIndex]
                    print(middleIndex, middleElement)
                    if middleElement < target:
                        sampleBounds[0] = middleIndex + 1
                    elif middleElement > target:
                        sampleBounds[1] = middleIndex - 1
                    else:
                        return middleIndex
            return -1







