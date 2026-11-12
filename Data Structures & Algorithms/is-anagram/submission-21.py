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
        # - Space = O(n + m) because the comparisons are being done in place
        #   and only input strings s and t are being updated and they only
        #   get smaller when there is a match. We are not considering each
        #   input string as free we would need to copy them into their
        #   temporary holders which we mutably update and change.
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
        # - If the full iteration of the charReps is done, then return true
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

        # Corrections by Claude formy solution:
        # - Bug:
        #   - When tChar isn’t in charReps, you set it to 1, but it should be 
        #     -1, because you’re subtracting. The result is still correct, 
        #     since 1 != 0 also triggers return False, but the logic doesn’t
        #     match what the dict means. Your own comment in 2a says 
        #     “subtract,” so the code and the comment disagree.
        #   - Simpler fix: if tChar isn’t in the dict, return False 
        #     immediately, since t has a character that s doesn’t.
        # - Brute force - real bug in approach:
        #   - Bug: your logic checks only that t ends up empty. Take s =
        #     "aab", t = "ab": the first a matches, the second a finds 
        #     nothing, b matches, and t is empty, so you’d return True. It 
        #     should be False. The fix is either a length check up front or 
        #     returning False when a character in s has no match. You also 
        #     need a break after the first match, or you’ll remove every copy
        #     of that character.
        #   - Space isn’t O(1). Python strings are immutable, so “removing” a
        #     character builds a new string, or you convert t to a list, 
        #     which is O(m) extra space. Each removal also costs O(m) time, 
        #     though it doesn’t change the O(n × m) bound.