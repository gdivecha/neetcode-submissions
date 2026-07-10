class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # - Let's look at the desired behavior we want and using that pattern we can come up with the algorithm
        #   and also, we need to keep in mind that we are solving a sliding window problwm:
        # - Using a sliding window approach:
        #   - e.g. 1) prices = [10,1,5,6,7,1]
        #     - Keeping the sliding window length at a a fixed value of 2
        #     - @ [10,1] -> Lower = 1, so we continue & bestProfit stays at 0
        #     - @ [1,5] -> Lower = 1, so we swap places so now prices = [10,5,1,6,7,1] & bestProfit = (5-1)>0 = 4
        #     - @ [1,6] -> Lower = 1, so we swap places so now prices = [10,5,6,1,7,1] & bestProfit = (6-1)>4= 5
        #     - @ [1,7] -> Lower = 1, so we swap places so now prices = [10,5,6,7,1,1] & bestProfit = (7-1)>5= 6
        #     - @ [1,1] -> Lower = Neither, so we continue & bestProfit stays at 6
        #   - e.g. 2) prices = [10,8,7,5,2]
        #     - @ [10,8] -> Lower = 8, so we continue & bestProfit stays at 0
        #     - @ [8,7] -> Lower = 7, so we continue & bestProfit stays at 0
        #       ...

        # Algorithm:
        # - maximumProfit = 0
        # - If length of prices > 1:
        #   - Iterate through each index of prices from 0 to range(len(prices)-1) meaning untilt he second last index:
        #     - difference = prices[currentIndex+1] - prices[currentIndex]
        #     - If difference > 0 and difference > maximumProfit:
        #       - maximumProfit = difference
        #       - Swap the elements at currentIndex and (currentIndex+1)
        # - Return maximumProfit

        maximumProfit = 0
        if len(prices) > 1:
            for index in range(len(prices)-1):
                difference = prices[index+1] - prices[index]
                if difference > 0:
                    lowerValue = prices[index]
                    higherValue = prices[index+1]
                    prices[index] = higherValue
                    prices[index+1] = lowerValue
                    maximumProfit = max(maximumProfit,difference)
                print(prices)
        return maximumProfit