class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # - First we need to create an array that simply
        #   holds all of the unique numbers from within nums
        #   which means e.g. [0,3,2,5,4,6,1,1] -> [0,3,2,5,4,6,1]
        #   and we name this array uniqueNums
        # - After some research, I foudn out that you can directly sue sets:
        #   - "A set in Python is an unordered collection of unique 
        #     elements. You use them primarily to eliminate duplicate
        #     values, perform fast membership tests (checking if an 
        #     item exists), and execute mathematical set operations 
        #     like unions and intersections."
        #   - "numbers = set([1, 2, 2, 3, 4, 4])  # Output: {1, 2, 3, 4}"
        #   - "For unordered collections that rely on a hash table 
        #     implementation, Python can look up items almost 
        #     instantly without scanning the entire collection.
        #     - Sets (set): O(1) average case.
        #     - Dictionaries (dict): O(1) average case when checking for keys."
        # - So let's try to decipher the kind of behaviour we want:
        #   - e.g. {5,1,1,3,7,4,6,5}:
        #     - We want = [3,4,5,6,7]
        #     - Set turns {5,1,1,3,7,4,6,5} into {5,1,3,7,4,6}
        #     - @ 5:
        #       - Add this to sequences = [5] -> [[5]]
        #       - Is 4 in set? Yes -> {5,1,3,7,6} -> [[5,4]]
        #       - Is 3 in set? Yes -> {5,1,7,6} -> [[5,4,3]]
        #       - Is 2 in set? No -> {1,7,6} -> [[5,4,3]]
        #     - @ 1:
        #       - Add this to sequences = [1] -> [[5,4,3],[1]]
        #       - Is 0 in set? No -> {7,6} -> [[5,4,3],[1]]
        #     - @ 7:
        #       - Add this to sequences = [7] -> [[5,4,3],[1],[7]]
        #       - Is 6 in set? Yes -> {7} -> [[5,4,3],[1],[7,6]]
        #       - Is 5 in set? No -> {} -> [[5,4,3],[1],[7,6]]
        #     - Create a dictionary called lowestInSubsequenceMapping = {}
        #       - Key = Lowest integer in a subarray
        #       - Value = The index of that subarray within the bigger array
        #     - Since we know that the logic so far works, let's try an example 
        #       where we have multiple disjointed sequences like so: 
        #       [[5,4,3],[1],[10,9,8],[7,6],[11]]
        #     - So, we use [[5,4,3],[1],[10,9,8],[7,6],[11,11]] to make {3:0, 1:1, 8:2, 6:3, 11:4}
        #       - How about we use highest value and lowest value inside the sub arrays
        #         so that we don't waste unnecessary space for numbers in betweem:
        #       - e.g.[[5,3],[1,1],[10,8],[7,6],[11,11]] and if we want, the total length of each 
        #         subarray we do 5-3+1 = 3 elements
        #     - Iterate through [[5,3],[1,1],[10,8],[7,6],[11,11]]:
        #       - @ [5,3] -> Is 6 in dict? Yes -> [[7,3],[1,1],[10,8],[7,3],[11,11]] and {3:0, 1:1, 8:2, 11:4}
        #       - @ [1,1] -> Is 2 in dict? Yes -> [[7,3],[1,1],[10,8],[7,3],[11,11]] and {3:0, 1:1, 8:2, 11:4}
        #       - @ [10,8] -> Is 11 in dict? Yes -> [[7,3],[1,1],[11,8],[7,3],[11,8]] and {3:0, 1:1, 8:2}
        #       - @ [7,3] -> Is 8 in dict ? Yes -> [[7,3],[1,1],[11,3],[11,3],[11,8]] and {3:0, 1:1}
        #       - @ [11,8] -> Is 12 in dict ? No -> [[7,3],[1,1],[11,3],[11,3],[11,8]] and {3:0, 1:1}
        #     - Iterate through [[7,3],[1,1],[11,3],[11,3],[11,8]] and trackt he largest length by doing (high-low+1)

        # Algorithm:
        # - Turn nums into a set of unique numebrs and call it uniqueNums
        # - Create an array called sequenceIntervals = [] that holds 2 element arrays of integers
        # - Create a set called valuesToAvoid that holds values that we wanna avoid which you will later see why
        #   - Essentially this is to avoid using set.remove(number) which has a O(1) time complexity on average
        #     but O(n) in worst case scenario for this reason:
        #     "In extremely rare cases, the time complexity can degrade to O(n), where n is the number of elements in
        #      the set. This only happens if your hash table suffers from massive hash collisions—meaning many different 
        #      keys accidentally hash to the exact same memory bucket, forcing Python to search through a linked 
        #      chain of elements linearly. Python's internal hashing algorithms are highly optimized, so you will almost 
        #      never encounter this in practice unless you deliberately design a custom object with a terrible __hash__ 
        #      function."
        # - Iterate through each uniqueNum in uniqueNums:
        #   - If currentNum not in valuesToAvoid:
        #     - Append the following to sequenceIntervals -> [currentNum, currentNum]
        #     - lowerValue = currentNum-1
        #     - While ((lowerValue in uniqueNums) and (lowerValue not in valuesToAvoid)):
        #       - sequenceIntervals[-1][1] = lowerValue
        #       - valuesToAvoid.add(lowerValue)
        #       - lowerValue-=1
        #     - valuesToAvoid.append(currentNum)
        # - Create a dictionary called lowestInSubsequenceMapping = {}
        #   - Key = Lowest integer in a subarray
        #   - Value = The index of that subarray within the bigger array
        # - Iterate through the sequenceIntervals and for each subsequence and its index:
        #   - lowestValueInSubsequence = currentSubsequence[-1]
        #   - lowestInSubsequenceMapping[lowestValueInSubsequence] = currentIndex
        # - For each subInterval in sequenceIntervals:
        #   - upperBound = subInterval[0]
        #   - nextValueToConnect = upperBound + 1
        #   - If (nextValueToConnect) in lowestInSubsequenceMapping:
        #     - upperBoundInHigherInterval = sequenceIntervals[lowestInSubsequenceMapping.get(nextValueToConnect)][0]
        #     - lowerBoundInLowerInterval = subInterval[1]
        #     - subInterval[0] = upperBoundInHigherInterval
        #     - sequenceIntervals[lowestInSubsequenceMapping.get(nextValueToConnect)][1] = lowerBoundInLowerInterval
        #     - lowestInSubsequenceMapping.pop(nextValueToConnect) and ignore the value immediately with 
        #       lowestInSubsequenceMapping.pop(nextValueToConnect, None) in Python
        # - Create an integer variable called currentLongestLength =  that keeps track of the running longest sequence length
        # - Iterate through sequenceIntervals one last time and for each interval:
        #   - upperBound = interval[0]
        #   - lowerBound = interval[1]
        #   - lengthOfCurrentSequence = upperBound - lowerBound + 1
        #   - If lengthOfCurrentSequence > currentLongestLength:
        #     - currentLongestLength = lengthOfCurrentSequence
        # - Return currentLongestLength

        uniqueNums = set(nums)
        valuesToAvoid = set()
        sequenceIntervals = []
        for currentNum in uniqueNums:
            if currentNum not in valuesToAvoid:
                sequenceIntervals.append([currentNum,currentNum])
                lowerValue = currentNum - 1
                while ((lowerValue in uniqueNums) and (lowerValue not in valuesToAvoid)):
                    sequenceIntervals[-1][1] = lowerValue
                    valuesToAvoid.add(lowerValue)
                    lowerValue-=1
                valuesToAvoid.add(currentNum)
        lowestInSubsequenceMapping = {}
        for currentIndex,currentSubsequence in enumerate(sequenceIntervals):
            lowestValueInSubsequence = currentSubsequence[-1]
            lowestInSubsequenceMapping[lowestValueInSubsequence] = currentIndex
        for subInterval in sequenceIntervals:
            upperBound = subInterval[0]
            nextValueToConnect = upperBound + 1
            if nextValueToConnect in lowestInSubsequenceMapping:
                upperBoundInHigherInterval = sequenceIntervals[lowestInSubsequenceMapping.get(nextValueToConnect)][0]
                lowerBoundInLowerInterval = subInterval[1]
                subInterval[0] = upperBoundInHigherInterval
                sequenceIntervals[lowestInSubsequenceMapping.get(nextValueToConnect)][1] = lowerBoundInLowerInterval
                lowestInSubsequenceMapping.pop(nextValueToConnect, None)
        currentLongestLength = 0
        for interval in sequenceIntervals:
            upperBound = interval[0]
            lowerBound = interval[1]
            lengthOfCurrentSequence = upperBound - lowerBound + 1
            if lengthOfCurrentSequence > currentLongestLength:
                currentLongestLength = lengthOfCurrentSequence
        return currentLongestLength






