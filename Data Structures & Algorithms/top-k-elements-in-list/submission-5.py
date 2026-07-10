class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # - Create a dictionary (numFrequency) that holds the following:
        #   - Key = integer that represents a number within nums
        #   - Value = frequency of that number occuring in nums
        # - Loop through the nums array and for each num:
        #   - If the num does not exist in numFrequency, then:
        #     - Add the key-value pair as follows:
        #       - Key = currentNum
        #       - Value = 1
        #   - Otherwise:
        #     - Increment the value associated to that currentNum key
        # - By this point, we should have a dictionary that holds
        #   the frequency of each number within the nums array
        #   - For e.g. [1,2,2,3,3,3] -> {1:1, 2:2, 3:3}
        #           or [7,8,2,7,2,9,9,9,9,3,2] -> {7:2, 8:1, 2:3, 9:4}
        
        # Trying out a couple approaches:
        # Approach #1 ---------------------------------------------------------
        # - Turn this into an array -> {7:2, 8:1, 2:3, 9:4} -> [7,8,2,9]
        #   - If we use a sliding window strategy:
        #     - [7,8] -> 7:2 and 8:1, we pick 7 as the winner
        #     - [7,2] -> 7:2 and 2:3, we pick 2 as the winner
        #     - [2,9] -> 2:3 and 9:4, we pick 9 as the winner
        #   - In the end, we pick the largest backwards so 9, then 2, then 7
        #   - If k = 1, then [9], if k = 2, then [9,2], if k = 3, then [9,2,7]
        # - Let's see whta we get if we had an example like:
        #   - e.g. [7,7,7,8,2,7,7,2,9,9,9,9,3,2] -> {7:5, 8:1, 2:3, 9:4}
        #     - We turn it into [7,8,2,9] again but now the window 
        #       results for each round look different
        #     - Use the strategy:
        #       - [7,8] -> 7:5 and 8:1, we pick 7 as the winner
        #       - [7,2] -> 7:5 and 2:3, we pick 7 as the winner
        #       - [7,9] -> 7:5 and 9:4, we pick 7 as the winner
        #     - If we now have to pick k = 3, we pick 3 7s which makes no sense
        #   - So we need a loser's bracket as well
        #     - Same example:
        #       - 8 lost in round 1 and 2 lost in round 2 -> 8:1 and 2:3 -> Pick 2
        #       - 2 lost in round 2 and 9 lost in round 3 -> 2:3 and 9:4 -> Pick 9
        #   - That is slightly iffy - What if we do the following instead fromt he get-go:
        #     - W = Null, L = Null
        #     - [7,8] -> 7:5 and 8:1 -> W = 7, L = 8
        #     - We have W and L both != Null, so:
        #       - Normal sliding window -> [8,2] -> 8:1,2:3 -> W
        # Approach #2 ---------------------------------------------------------
        # - What if we tried a true sliding window?
        #   - E.g. {7:5, 8:1, 2:3, 9:4} -> [7,8,2,9] and k = 2
        #     - [7,8] -> 7:5,8:1 -> Largest = 7
        #     - [8,2] -> 8:1,2:3 -> Largest = 2
        #     - [2,9] -> 2:3,9:4 -> Largest = 9
        #   - E.g. {7:5, 8:1, 2:3, 9:4} -> [7,8,2,9] and k = 3
        #     - [7,8,2] -> 7:5,8:1,2:3 -> Largest = 7
        #     - [8,2,9] -> 8:1,2:3,9:4 -> Largest = 9
        # - Just realized that the window size should have nothing to do with k
        #   - So this flopped
        # Approach #3 ---------------------------------------------------------
        # - Turn the dictionary keys into a list or array of keys
        #   - E.g. {7:6, 8:1, 2:3, 9:5, 3:7, 5:4} -> [7,8,2,9,3,5] and k = 3 for e.g.
        # - We want mostFrequentNums = [] in the e.g.
        #   1. We look at 7 in [7,8,2,9,3,5], mostFrequentNums = [7], indexOfLowestElement = 0, (len(mostFrequentNums)=1) < (k=3) yet
        #   2. We look at 8 in [7,8,2,9,3,5], mostFrequentNums = [7,8], indexOfLowestElement = 1, (len(mostFrequentNums)=2) < (k=3) yet
        #   3. We look at 2 in [7,8,2,9,3,5], mostFrequentNums = [7,8,2], indexOfLowestElement = 1, (len(mostFrequentNums)=3) == (k=3) finally
        #   4. We look at 9 in [7,8,2,9,3,5], mostFrequentNums = [7,9,2], indexOfLowestElement = 2, (len(mostFrequentNums)=3) == (k=3) from before
        #   5. We look at 3 in [7,8,2,9,3,5], mostFrequentNums = [7,9,3], indexOfLowestElement = 1, (len(mostFrequentNums)=3) == (k=3) from before
        #   6. We look at 5 in [7,8,2,9,3,5], mostFrequentNums = [7,9,3], indexOfLowestElement = 1, (len(mostFrequentNums)=3) == (k=3) from before
        # - This is the kind of behavior we want:
        #   - When len(mostFrequentNums) < k:
        #     - We populate mostFrequentNums and keep track of the indexOfLowestElement
        #   - When len(mostFrequentNums) == k:
        #     - If numFrequency.get(mostFrequentNums[indexOfLowestElement]) < numFrequency.get(currentNum):
        #       - mostFrequentNums[indexOfLowestElement] = currentNum
        #       - indexOfLowestElement is no longer the same as before because we switched out the element with the highest
        #         !!!!! There needs to be a recalibration process done to find new lowest !!!!!
        #     - Else (numFrequency.get(mostFrequentNums[indexOfLowestElement]) > numFrequency.get(currentNum)):
        #       - We do nothing because mostFrequentNums is not supposed to change
        # - So our only concern is to figure out how to easily recalibrate without entering O(n^2) territory
        # Approach #4 ---------------------------------------------------------
        # - {7:6, 8:1, 2:3, 9:5, 3:7, 5:4} -> [7,8,2,9,3,5]:
        # - What if we create a new array called frequencyTracker of length len(nums) and initialize all values to be
        #   numerically impossible values like [null,null,null,null,null,null]
        #   - We iterate through the dictionary keys and for each currentKey:
        #     - frequencyTracker[numFrequency.get(currentKey)] = currentKey
        # - We set a count variable to 0
        # - We create an array called mostFrequentElements = [] that holds numbers
        # - We iterate through the frequencyTracker array backwards and for each num we do:
        #   - If (currentNum != Null) and (count<k):
        #     - mostFrequentElements.append(currentNum)
        # - Return mostFrequentElements

        # numFrequency = {}
        # for currentNum in nums:
        #     if currentNum not in numFrequency.keys():
        #         numFrequency[currentNum] = 1
        #     else:
        #         numFrequency[currentNum]+=1
        # keyList = list(numFrequency)
        # frequencyTracker = [None for num in (nums+[None])]
        # for currentKey in keyList:
        #     frequencyTracker[numFrequency.get(currentKey)] = [currentKey]
        # count = 0
        # i = len(frequencyTracker)-1
        # j = 0
        # print(frequencyTracker)
        # mostFrequentElements = []
        # while (count<k):
        #     if frequencyTracker[i] != None:
        #         if len(frequencyTracker[i]) > 1 and j < len(frequencyTracker[i]):
        #             mostFrequentElements.append(frequencyTracker[i][j])
        #             j+=1
        #             count+=1
        #         elif len(frequencyTracker[i]) > 1:
        #             j = 0
        #         else:
        #             mostFrequentElements.append(frequencyTracker[i][0])
        #         i-=1
        # return mostFrequentElements




        # - Create a dictionary called frequencyTracker = {}
        #   - Key = Frequency as an integer that says how many times a number is repeated
        #   - Value = Array of integers whose frequency corresponds to the key
        # - Create a dictionary called numFrequency - {}
        #   - Key = Number within nums
        #   - Value = Frequency of the corresponding num within nums
        # - Track this e.g. nums = [1,2,1,2,3,3,3,4,4,4,5], k = 2
        # - Iterate through the entire array nums and for each num:
        #   - If num in numFrequency.keys():
        #     - numFrequency[num] += 1
        #   - Else:
        #     - numFrequency[num] = 1
        #   - Tracking above example: numFrequency = {1:2, 2:2, 3:3, 4:3, 5:1}
        # - Iterate through each key value pair in numFrequency dictionary:
        #   - If the value (frequency fo the current key num) is not in frequencyTracker:
        #     - frequencyTracker[value] = [key]
        #   - Else:
        #     - frequencyTracker[value].append(key)
        #   - Tracking above example: frequencyTracker = {2:[1,2], 3:[3,4], 1:[5]}
        # - Iterate through all the keys within frequencyTracker and find the highest frequency
        # - count = 0
        # - topKFrequentElements = []
        # - Iterate through values from highestFrequency downwards by 1 starting at highestFrequency:
        #   - If currentFrequency is in frequencyTracker:
        #     - Iterate through each value array corresponding to the frequency:
        #       - If count <k:
        #         - topKFrequentElements.append(value)
        #         - count+=1
        #       - Else:
        #         - return topKFrequentElements

        frequencyTracker = {}
        numFrequency = {}
        for num in nums:
            if num not in numFrequency.keys():
                numFrequency[num] = 1
            else:
                numFrequency[num]+=1
        for num,frequency in numFrequency.items():
            if frequency not in frequencyTracker:
                frequencyTracker[frequency] = [num]
            else:
                frequencyTracker[frequency].append(num)
        highestFrequency = 0
        for frequency in frequencyTracker.keys():
            if frequency > highestFrequency:
                highestFrequency = frequency
        count = 0
        topKFrequentElements = []
        print(frequencyTracker)
        print(numFrequency)
        print(highestFrequency)
        for frequency in range(highestFrequency,0,-1):
            if frequency in frequencyTracker:
                for num in frequencyTracker[frequency]:
                    if count < k:
                        topKFrequentElements.append(num)
                        count+=1
                    else:
                        return topKFrequentElements
        return topKFrequentElements























