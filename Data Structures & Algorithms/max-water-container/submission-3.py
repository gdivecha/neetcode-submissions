class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # - currentHighestArea = 0
        # - i = 0
        # - j = len(heights)-1
        # - We come in from btoh sides and we need to fo this
        # - While (i<j):
        #   - If heights[i]==0:
        #     - i+=1
        #     - Continue
        #   - If heights[j]==0:
        #     - j-=1
        #     - Continue
        #   - lowerHeight = min(heights[i],heights[j])
        #   - currentArea = lowerHeight * (j-i)
        #   - currentHighestArea = currentArea if currentArea>currentHighestArea else currentHighestArea
        #   - If height[i]>height[j]:
        #     - j-=1
        #   - Else if height[j]>height[i]:
        #     - i+=1
        #   - Else:
        #     - i+=1
        #     - j-=1

        # currentHighestArea = 0
        # i = 0
        # j = len(heights) - 1
        # while i<j:
        #     if heights[i]==0:
        #         i+=1
        #         continue
        #     if heights[j]==0:
        #         j-=1
        #         continue
        #     lowerHeight = min(heights[i],heights[j])
        #     currentArea = lowerHeight * (j-i)
        #     currentHighestArea = currentArea if currentArea>currentHighestArea else currentHighestArea
        #     if heights[i]>heights[j]:
        #         j-=1
        #     elif heights[j]>heights[i]:
        #         i+=1
        #     else:
        #         i+=1
        #         j-=1
        # return currentHighestArea

        # Streamlining:
        currentHighestArea = 0
        i = 0
        j = len(heights) - 1
        while i<j:
            lowerHeight = min(heights[i],heights[j])
            currentArea = lowerHeight * (j-i)
            currentHighestArea = max(currentArea, currentHighestArea)
            if heights[i]>heights[j]:
                j-=1
            elif heights[j]>heights[i]:
                i+=1
            else:
                i+=1
                j-=1
        return currentHighestArea
