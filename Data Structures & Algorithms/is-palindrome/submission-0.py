class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach #1 ----------------------------------------
        # - We could have 2 pointers i and j
        # - i = 0 and j = len(s) - 1
        # - While (i<j):
        #   - If s[i] != s[j]:
        #     - Return False
        #   - i++ and j--
        # - Return True

        onlyAlphanumericString = "".join(char.lower() for char in s if char.isalnum())
        i = 0
        j = len(onlyAlphanumericString)-1
        while i<j:
            print(i,j)  
            print(onlyAlphanumericString[i] , onlyAlphanumericString[j] )
            if onlyAlphanumericString[i] != onlyAlphanumericString[j]:
                return False
            i+=1
            j-=1
        return True