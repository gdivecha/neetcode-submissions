class MinStack:

    def __init__(self):
        self.stack = []
        self.currentMin = None

    def push(self, val: int) -> None:
        # - When we push a value onto the stack, we need to do the following:
        #   - If currentMin isn't null, then:
        #     - We make the minimum of these 2 equal to currentMin: currentMin and val
        #   - Otherwise:
        #     - currentMin = val
        #   - stack.append([val,currentMin])
        #   - Return null
        self.currentMin = min(self.currentMin,val) if self.currentMin!=None else val
        print("Current Min",  self.currentMin)
        self.stack.append([val,self.currentMin])
        return None

    def pop(self) -> None:
        # - This is where the difficulty is introduced
        #   - Because we want a O(1) pop function, we need a mechanism in place that
        #     updates the currentMin IV in the class whenever we pop the top value
        #     - Usually, this mechanism woudl introduce O(n) compexity whcih we don't want
        #     - So we will probably need to work with the push function to make sure
        #       that the sorting happens right from the get-go instead of pop doing all the work
        # - What if we do this:
        #   - When a new value is added, we do the  in addition to the stuff we do for pop explained above:
        #     - e.g. ["push", 1, "push", 2, "push", 4", "push", "3", "push", "0", "push", "-1"]
        #       - stack = [] where each entry is a 2 element array -> [a,b] where a = number that is pushed
        #         and b = currentMin at that point in time  
        #       - @ 1 -> stack = [[1,1]]
        #       - @ 2 -> stack = [[1,1],[2,1]]
        #       - @ 4 -> stack = [[1,1],[2,1],[4,1]]
        #       - @ 3 -> stack = [[1,1],[2,1],[4,1],[3,1]]
        #       - @ 0 -> stack = [[1,1],[2,1],[4,1],[3,1],[0,0]]
        #       - @ -1 -> stack = [[1,1],[2,1],[4,1],[3,1],[0,0],[-1,-1]]
        #     - So if we pop one the stack, the minimum is retained 
        # - Algorithm:
        #   - stack.pop()
        #   - latestEntry = stack[-1]
        #   - currentMin = latestEntry[1]
        #   - Return null
        if self.stack:
            self.stack.pop()
        if self.stack:
            self.currentMin = self.stack[-1][1]
        else:
            self.currentMin = None
        return None

    def top(self) -> int:
        # - Return stack[-1][0]
        topValue = None
        if self.stack:
            topValue = self.stack[-1][0]
        return topValue

    def getMin(self) -> int:
        # - Return stack[-1][1]
        minValue = None
        if self.stack:
            minValue = self.stack[-1][1]
        print(minValue)
        return minValue
        
