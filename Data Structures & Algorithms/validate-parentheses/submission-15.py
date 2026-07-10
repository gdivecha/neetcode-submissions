class Solution:
    def isValid(self, s: str) -> bool:
        # - Create a dictionary (closedToOpenMapping) that holds the following:
        #   - {"}":"{", "]":"[", ")":"("}
        # - We must use a stack for its LIFO functionality
        # - We create a stack = []
        # - We iterate through the string s and for each bracket:
        #   - If the bracket does not exist in the closedToOpenMapping.keys():
        #     - Append that bracket to the stack
        #   - Otherwise:
        #     - Pop the stack
        #     - If the popped value != closedToOpenMapping.get(current bracket):
        #       - Return false
        # - Return true

        closedToOpenMapping = {
            "}":"{", 
            "]":"[", 
            ")":"("
        }
        stack = []
        for bracket in s:
            if bracket not in closedToOpenMapping.keys():
                stack.append(bracket)
            else:
                if not stack:
                    return False
                lastIn = stack.pop()
                if lastIn != closedToOpenMapping.get(bracket):
                    return False
        return not stack
        