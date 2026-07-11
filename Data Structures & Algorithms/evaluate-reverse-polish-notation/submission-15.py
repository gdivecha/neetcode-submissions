class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # - Let's try to figure out the desired behavior here keeping
        #   in mind that we need to use a stack
        #   - e.g. tokens = ["7","3","+","4","2","-","*"]
        #     - We want (7+3)*(4-2)
        #     - stack = []
        #     - @ "7" -> stack.append("7") -> stack = ["7"]
        #     - @ "3" -> stack.append("3") -> stack = ["7","3"]
        #     - @ "+" -> formula += (sum up stack.pop() x 2 times) -> stack.append(sum=10) -> stack = ["10"]
        #     - @ "4" -> stack.append("4") -> stack = ["10","4"]
        #     - @ "2" -> stack.append("2") -> stack = ["10","4","2"]
        #     - @ "-" -> formula += (sum up stack.pop() x 2 times) -> stack.append(difference=2) -> stack = ["10","2"]
        #     - @ "*" -> formula += (sum up stack.pop() x 2 times) -> stack.append(product=20) -> stack = ["20"]

        # Algorithm:
        # - stack = []
        # - Iterate through tokens and for each token:
        #   - If the token is a number:
        #     - stack.append(token)
        #   - Else:
        #     - operand2 = stack.pop()
        #     - operand1 = stack.pop()
        #     - formula = (operand1 token operand2)
        #     - stack.append(eval(formula))
        # - return stack[0]

        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                operand2 = stack.pop()
                operand1 = stack.pop()
                formula = f"({operand1}){token}({operand2})"
                print(formula)
                stack.append(int(eval(formula)))
                print(stack)
        return stack[0]

        # tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # 1
