class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 1a. Brute Force:
        # - Iterate through the s string and for each sChar:
        #   - Iterate through the t string:
        #     - If there is a tChar that matches sChar, then:
        #       - Remove that element from the string
        #     - Otherwise:
        #       - Continue
        # - Once the s string is done iterating, then evaluate the
        #   remaining t string:
        #   - If t string is an empty string:
        #     - Return true
        #   - Otherwise:
        #     - Return false
        #
        # 1b. Complexity:
        # - Time = O(n x m) where len(s) = n and len(t) = m, because for 
        #   each character in one string, we have to iterate through the
        #   other string
        # - Space = O(1) because the comparisons are being done in place
        #   and only input strings s and t are being updated and they only
        #   get smaller when there is a match
        #
        # 1c. Implementation:
        # - Skipped

        # 2a. Optimized Approach
        # - Create a dict called charReps = {}
        #   - By the way this is also what a hash table is generally but
        #     the implementation of this within python is via dictionary
        # - Iterate through s string and for each sChar:
        #   - If sChar does not exist within sCharReps's list of keys:
        #     - Make a key value pair (sChar: 1)
        #   - Otherwise:
        #     - Add one to the value of that key (sChar: x + 1)
        # - Iterate through t string and for each tChar:
        #   - If tChar does not exist within tCharReps's list of keys:
        #     - Make a key value pair (tChar: 1)
        #   - Otherwise:
        #     - Subtract one to the value of that key (tChar: x - 1)
        # - Iterate through each key-value pair within the dict and for each:
        #   - If the value of the current key != 0:
        #     - Return false
        #   - Else:
        #     - Return true
        #
        # 2b. Complexity:
        # - Time = O(n + m), because we go through s once and m once and then
        #   the dict once after
        # - Space = O(n + m) worst case, where len(s) = n and len(t) = m,
        #   because in the worse case, we have 2 completely different words
        #   with every single letter different across both s and t, which
        #   means charReps gets a key value pair for each unique letter
        #   across both s and t
        #
        # 2c. Implementation:
        # - Done below:

        charReps = {}
        for sChar in s:
            if sChar in charReps:
                charReps[sChar] += 1
            else:
                charReps[sChar] = 1
        for tChar in t:
            if tChar in charReps:
                charReps[tChar] -= 1
            else:
                charReps[tChar] = 1
        for repetition in charReps.values():
            if repetition != 0:
                return False
        return True


