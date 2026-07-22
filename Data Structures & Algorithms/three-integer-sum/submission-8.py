class Solution:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    # def get_unique_3_element_arrays(self,list_of_arrays):
    #     return [list(t) for t in {tuple(a): None for a in list_of_arrays if len(a) == 3}]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # - Let's try to come up with a solution keeping in mind the
        #   following:
        #   - 2 pointer solution required
        #   - Time Complexity should be O(n^2) where n = size of input array
        #   - Space Complexity should be O(1) 
        # - If O(n^2) is allowed, we could put sorting into the mix as well
        #   - Here are some of the sort functions and their characteristics:
        #     | Sorting function | Best Case | Worst Case | Space Comp |
        #     | list.sort()      | O(n)      | O(nlogn)   | O(n)       |
        #     | Insertion Sort   | O(n)      | O(n^2)     | O(1)       |
        #     | Bubble Sort      | O(n)      | O(n^2)     | O(1)       |
        #     | Selection Sort   | O(n^2)    | O(n^2)     | O(1)       |
        #   - As we can see, the built in sort function takes more
        #     space complexity than what we are looking for
        #   - We could just  make our own insertion sort algorithm
        # - Let's say we sort the following - what do we get:
        #   - e.g. nums = [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
        #   - Let's look at the 2 pointer approach with what we have:
        #     - @ i=0,j=5 -> -4 & 2:
        #       - Add up to -2 and we need +2 to get final value of 0
        #       - We iterate through the remaining section of the array
        #         [-1,-1,0,1] from left to right to find +2
        #       - No +2 found which neutralizes the -2
        #       - Since the value we needed to neutralize was -2, we
        #         increase i to 1
        #     - @ i=1,j=5 -> -1 & 2:
        #       - Add up to 1 and we need -1 to get final value of 0
        #       - We iterate through the remaining section of the array
        #         [-1,0,1] from left to right to find -1
        #       - -1 found to neutralize the +1 sum
        #       - We output [-1,2,-1] 
        #       - Since the value we needed to neutralize was +1, we
        #         decrease j by 1 so j = 4
        #     - @ i=1,j=4 -> -1 & 1:
        #       - Add up to 0 and we need 0 to get final value of 0
        #       - We iterate through the remaining section of the array
        #         [-1,0] from left to right to find -1
        #       - 0 found to neutralize the 0 sum
        #       - We output [-1,1,0] 
        #       - Since the value we needed to neutralize was 0, we
        #         decrease j by 1 and increase i by 1 so i = 2 and j = 3

        # Algorithm:
        # - Sort the arry first using insertion sort
        # - triplets = []
        # - i = 0
        # - j = len(nums)-1
        # - while i<(j-1):
        #   - sumToNeutralize = nums[i] + nums[j]
        #   - neutralizer = 0 - sumToNeutralize
        #   - for value between i and j:
        #     - if value == neutralizer:
        #       - triplets.add([nums[i],nums[j],value])
        #       - continue
        #   - if sumToNeutralize < 0:
        #     - i+=1 
        #   - else if sumToNeutralize > 0:
        #     - j-=1
        #   - else:
        #     - i+=1 and j-=1
        # - Return triplets

        # sortedNums = self.insertionSort(nums)
        # triplets = set()
        # i = 0
        # j = len(nums)-1
        # while i<(j-1):
        #     sumToNeutralize = nums[i] + nums[j]
        #     neutralizer = 0 - sumToNeutralize
        #     for value in nums[i+1:j]:
        #         if value == neutralizer:
        #             triplets.add((nums[i],nums[j],value))
        #             continue
        #     if sumToNeutralize < 0:
        #         i+=1
        #     elif sumToNeutralize > 0:
        #         j-=1
        #     else:
        #         i+=1
        #         j-=1
        # return [list(triplet) for triplet in triplets]

        # - So, 18/26 test cases pass and here's what GPT had to propose:
        #   - First of all I got the idea to make triplets a set() from
        #     gemini and that a array is unhashable in a set so one
        #     needs to use (nums[i],nums[j],value) instead of
        #     [nums[i],nums[j],value] when adding it to the set
        #   - Also, if we wanna turn a set value (nums[i],nums[j],value)
        #     into a list or array, then we have to do this:
        #     [list(triplet) for triplet in triplets] typecasting
        # - Instead of while outside of a for loop, where we bypass
        #   many of the combinations when we do i+=1 and j-=1, we do the opposite
        # - Let's try it out

        self.insertionSort(nums)
        triplets = set()
        i = 0
        j = len(nums)-1
        for index in range(len(nums)-2):
            leftPointer = index + 1
            rightPointer = len(nums) - 1
            while leftPointer < rightPointer:
                anchor = nums[index]
                leftVal = nums[leftPointer]
                rightVal = nums[rightPointer]
                total = anchor + leftVal + rightVal
                if total == 0:
                    triplets.add((anchor,leftVal,rightVal))
                    leftPointer += 1
                    rightPointer -= 1
                elif total < 0:
                    leftPointer += 1
                elif total > 0:
                    rightPointer -= 1
        return [list(triplet) for triplet in triplets]

