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

        # Corrections from Claude:
        # Infinite loop risk. while k > 0 has no stop if count drops 
        # below 0 and k is still positive, because nothing is found and k 
        # never changes. The problem’s constraints stop that from 
        # happening, but a for count in range(len(nums), 0, -1) 
        # loop can’t hang, and a bug there would just return a short
        # list. Use that, and break once 
        # you have enough.

        # It relies on the uniqueness guarantee. Your loop adds a whole 
        # group at once. If a group straddles k, you’d return more than k 
        # elements. That’s fine here because the problem guarantees 
        # it can’t happen, but in an interview where the guarantee 
        # isn’t stated, stop when the result has k elements and 
        # return res[:k].

        # A list is a more common bucket than a dict. buckets = [[] 
        # for _ in range(len(nums) + 1)] with buckets[count].append(num) 
        # skips the in check entirely, and it’s the form most people 
        # write for this problem.

        # Your brute force notes say to sort a list of frequencies 
        # and then recover the number for each one. That loses the 
        # link between a number and its count. Sort the (count, num) 
        # pairs instead, 
        # for example sorted(numCount.items(), key=lambda x: x[1], 
        # reverse=True)[:k].


