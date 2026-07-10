class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
                        break
        return topKFrequentElements
