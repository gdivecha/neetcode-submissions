class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force Approach:
        # - We create a dictionary called numCount = {}
        # - Iterate through each num in nums:
        #   - If num is a key in numCount, then:
        #     - numCount[num] += 1
        #   - Else:
        #     - numCount[num] = 1
        # - This will turn nums = [1,2,2,3,3,3] for e.g.
        #   into numCount = {1:1, 2:2, 3:3}
        # - We can then create a list that holds all the frewuencies
        #   or counts and sort it from highest to lowest
        # - Then we can iterate through that list as we decrement
        #   k by 1 each time until k = 0 and as we do that
        #   the num associated to that frequency is picked
        # 
        # Complexity:
        # - Time = O(n + nlogn) = O(nlogn) because nlogn would be
        #   used to sort the repetitions in worst case scenario
        # - Space = O(n) because of the dictionary and the list
        #   that holds the reps

        # We do want to find a way to get O(n) time
        # - We keep this:
        # - We create a dictionary called numCount = {}
        # - Iterate through each num in nums:
        #   - If num is a key in numCount, then:
        #     - numCount[num] += 1
        #   - Else:
        #     - numCount[num] = 1
        # - This will turn nums = [1,2,2,3,3,3] for e.g.
        #   into numCount = {1:1, 2:2, 3:3}
        #
        # Then we need something that optimizes the approach:
        # - "The test cases are generated such that the answer 
        #   is always unique." which means if we had 
        #   an e.g. [1,2,2,2,3,3,3], then the k we are given
        #   can never be = 1 in the test cases because that would
        #   mean then the algo would need to pick between 2 and 3
        # - What if we turn numCount = {1:5, 2:3, 4:3, 3:2} for e.g. into
        #   countToNumMap = {5:[1], 3:[2,4], 2:[3]}, k that is given 
        #   has to be either = 1 or >= 3 and can never be 2 because
        #   if it were, then we'd have to pick betwen 2 and 4 after 1
        # - This would still need sorting then...
        #   
        # Another Approach:
        # - What if we use array representation somehow:
        # - If we have {1:5, 2:3, 4:3, 3:2}, then could this work?
        #   - Indices -> [0,1,2,3,4,5,...]
        #   - Values ->  [0,5,3,2,3,0,...]
        #
        # - Had to look at my past submission:
        # - We take this approach countToNumMap = {5:[1], 3:[2,4], 2:[3]}
        #   and since we know the highest total number of repetitions
        #   a number can have is literally len(nums) in case there's
        #   only 1 number repeated len(nums) times
        # - What we do is that if we go through the list of numbers 
        #   in range starting at len(nums) and go downwards
        #   and for each number, we check whether that number exists as
        #   the key within countToNumMap, we can get its list
        #   and append that list to the running final list to be returned
        #   and as we do that, we decrement k by 1 each time until k = 0

        numToCountMap = defaultdict(int)
        for num in nums:
            numToCountMap[num] += 1
        
        countToNumMap = defaultdict(list)
        for num in numToCountMap:
            countToNumMap[numToCountMap[num]].append(num)

        count = len(nums)
        topKFrequentElements = []
        while k>0:
            if count in countToNumMap:
                topKFrequentElements += countToNumMap[count]
                k -= len(countToNumMap[count])
            count -=1 

        return topKFrequentElements


