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

        # onlyAlphanumericString = "".join(char.lower() for char in s if char.isalnum())
        # i = 0
        # j = len(onlyAlphanumericString)-1
        # while i<j:
        #     print(i,j)  
        #     print(onlyAlphanumericString[i] , onlyAlphanumericString[j] )
        #     if onlyAlphanumericString[i] != onlyAlphanumericString[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True

        # Approach #2 ----------------------------------------
        # - We can use a stack and a queue
        # - Stacks are LIFO and queues are FIFO
        # - We create a stack = [] and queue = []
        # - For each character in the alphanumeric only string of s:
        #   - We use the data structures behavioral characteristic to
        #     insert the character
        # - Once both are already filled, we then loop through the stack
        #   or the queue from left to right and we check whether both
        #   data structures have the same character at the exact same index
        #   - Even if one character doesn't match, then return False
        # - Once loop ends, return True

        onlyAlphanumericString = "".join(char.lower() for char in s if char.isalnum())
        stack = []
        queue = deque()
        for character in onlyAlphanumericString:
            stack.append(character)
            queue.append(character)
        while len(stack) > 0:                
            lastInFromStack = stack.pop()
            firstInFromQueue = queue.popleft()
            if lastInFromStack != firstInFromQueue:
                return False
        return True










