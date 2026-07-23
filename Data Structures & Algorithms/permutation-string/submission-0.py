class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # - Let's keep in mind the following:
        #   - You should aim for a solution with 
        #     O(n) time and O(1) space, where n is 
        #     the maximum of the lengths of the two strings.
        #   - We are dealing with a sliding window problem
        # - Let's make the use of ASCII value and prime numbers
        #   - Assign a prime number to each alphabet

        # - Desired behavior:
        #   - s1 = "abc", s2 = "lecabee"
        #   - e.g. s1HashVal = 1237
        #   - trackingStrCount = 0
        #   - Iterate through "lecabee"
        #     - @ index = 0 -> s2[0] = l -> "l":
        #       - s2HashVal = 233
        #       - trackingStrCount = 1
        #       - Is trackingStrCount == len(s1)? No
        #     - @ index = 1 -> s2[1] = e -> "le":
        #       - s2HashVal = 671
        #       - trackingStrCount = 2
        #       - Is trackingStrCount == len(s1)? No
        #     - @ index = 2 -> s2[2] = c -> "lec":
        #       - s2HashVal = 837
        #       - trackingStrCount = 3
        #       - Is trackingStrCount == len(s1)? Yes
        #         - Is s1HashVal == s2HashVal? No
        #           - firstLetterInTrackingStr = s2[index - (trackingStrCount - 1)] = "l"
        #           - s2HashVal -= (ASCII(firstLetterInTrackingStr) * primeEquivalents.get(firstLetterInTrackingStr))
        #                        = 604
        #           - trackingStrCount = 2
        #     - @ index = 3 -> s2[3] = a -> "eca":
        #       - s2HashVal = 767
        #       - trackingStrCount = 3
        #       - Is trackingStrCount == len(s1)? Yes
        #         - Is s1HashVal == s2HashVal? No
        #           - firstLetterInTrackingStr = s2[index - (trackingStrCount - 1)] = "e"
        #           - s2HashVal -= (ASCII(firstLetterInTrackingStr) * primeEquivalents.get(firstLetterInTrackingStr))
        #                        = 567
        #           - trackingStrCount = 2
        #     - @ index = 4 -> s2[4] = b -> "cab":
        #       - s2HashVal = 973
        #       - trackingStrCount = 3
        #       - Is trackingStrCount == len(s1)? Yes
        #         - Is s1HashVal == s2HashVal? Yes
        #           - return True
        #     - Return False otherwise



        # - Algorithm:
        #   - primeEquivalents = {'a':2, 'b':3, ...}
        #   - s1HashVal, s2HashVal = 0
        #   - Iterate through s1 characters:
        #     - s1HashVal += (ASCII(character) * primeEquivalents.get(character))
        #   - trackingStrCount = 0
        #   - for each character and its index in s2
        #     - s2HashVal += (ASCII(character) * primeEquivalents.get(character))
        #     - trackingStrCount += 1
        #     - If trackingStrCount == len(s1HashVal):
        #       - If s1HashVal == s2HashVal:
        #         - Return True
        #       - Else:
        #         - trackingStrCount -= 1
        #         - firstLetterInTrackingStr = s2[index - trackingStrCount]
        #         - s2HashVal -= (ASCII(firstLetterInTrackingStr) * primeEquivalents.get(firstLetterInTrackingStr))
        #   - Return False

        primeEquivalents = {
            "a": 2,  "b": 3,  "c": 5,  "d": 7,  "e": 11, 
            "f": 13, "g": 17, "h": 19, "i": 23, "j": 29, 
            "k": 31, "l": 37, "m": 41, "n": 43, "o": 47, 
            "p": 53, "q": 59, "r": 61, "s": 67, "t": 71, 
            "u": 73, "v": 79, "w": 83, "x": 89, "y": 97, 
            "z": 101
        }
        s1HashVal = s2HashVal = trackingStrCount = 0
        for character in s1:
            s1HashVal += (ord(character) * primeEquivalents.get(character))
        for index,character in enumerate(s2):
            s2HashVal += (ord(character) * primeEquivalents.get(character))
            trackingStrCount += 1
            if trackingStrCount == len(s1):
                if s1HashVal == s2HashVal:
                    return True
                else:
                    trackingStrCount -= 1
                    firstLetterInTrackingStr = s2[index - trackingStrCount]
                    s2HashVal -= (ord(firstLetterInTrackingStr) * primeEquivalents.get(firstLetterInTrackingStr))
        return False