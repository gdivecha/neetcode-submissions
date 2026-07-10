class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # - Create a dictionary called charReps
        # - charReps contains key value pairs:
        #   - key = character
        #   - value = repetitions of the current character
        # - We loop through the first string:
        #   - If the current character does not exist in the list of keys in the dict:
        #     - Add the key = char and value for it being = 1
        #   - Otherwise:
        #     - Increment the value of the current character key in the dict
        # - We loop through the second string:
        #   - If the current character does not exist in the list of keys in the dict:
        #     - Return False
        #   - Else if the current character does exist:
        #     - Decrement the value of the current character key in the dict
        #   - If the value for the current character key reaches < 0:
        #     - Return False
        # - If the loop finishes, then return True

        if(len(s)!=len(t)):
            return False
        charReps = {}
        for char in s:
            if char not in charReps.keys():
                charReps[char] = 1
            else:
                charReps[char]+=1
        for char in t:
            if char not in charReps.keys():
                return False
            else:
                charReps[char]-=1
        for key in charReps.keys():
            if charReps.get(key)!=0:
                return False                
        return True


            