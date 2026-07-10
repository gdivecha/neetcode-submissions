class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Let's try to find the behaviour we want:
        # - e.g. nums = [1,2,4,6]
        #   - When @ index = 0, nums[0] = 1; we want 2 x 4 x 6 = 48
        #   - When @ index = 1, nums[1] = 2; we want 1 x 4 x 6 = 24
        #   - When @ index = 2, nums[2] = 4; we want 1 x 2 x 6 = 12
        #   - When @ index = 3, nums[3] = 6; we want 1 x 2 x 4 = 8
        # - What if we do this:
        #   - For dict1:
        #     - @ i = 0 -> dict1 = {0:[1,1]} 
        #     - @ i = 1 -> dict1 = {0:[1,1], 1:[2,2]} 
        #     - @ i = 2 -> dict1 = {0:[1,1], 1:[2,2], 2:[4,8]} 
        #     - @ i = 3 -> dict1 = {0:[1,1], 1:[2,2], 2:[4,8], 3:[6,48]}
        #   - Now from rigth to left for dict 2:
        #     - @ i = 3 -> dict1 = {3:[6,6]} 
        #     - @ i = 2 -> dict1 = {3:[6,6], 2:[4,24]} 
        #     - @ i = 3 -> dict1 = {3:[6,6], 2:[4,24], 1:[2:48]}
        #     - @ i = 3 -> dict1 = {3:[6,6], 2:[4,24], 1:[2:48], 0:[1,48]}
        #   - We have the 2 dicts here:
        #     - dict1 = {0:[1,1], 1:[2,2], 2:[4,8], 3:[6,48]}
        #     - dict2 = {3:[6,6], 2:[4,24], 1:[2:48], 0:[1,48]}
        #             = {0:[1,48], 1:[2:48], 2:[4,24], 3:[6,6]}
        #   - Now, if we want the outputs:
        #     - @ i = 0 -> (Nothing to the left = 1) x (right =  dict2.get(0)[1] = 48) = 48
        #     - @ i = 1 -> (left = dict1.get(0)[1] = 1) x (right = dict2.get(2)[1] = 24) = 24
        #     - @ i = 2 -> (left = dict1.get(1)[1] = 2) x (right = dict2.get(3)[1] = 6) = 12
        #     - @ i = 1 -> (left = dict1.get(2)[1] = 8) x (Nothing to the right = 1) = 8
        # - Now, we know this works so let's improve it and also make it more streamlined
        #   - Let's work with 1 dictionary and we also don't need to write down
        #     the value at that index intot he value for the key in the dict
        #   - Also, we could just use an array instead of a dictionary but
        #     I'm using this for the ease of the data structure to go throught when
        #     evaluating the terms backwards for dictionaries as opposed to arrays
        #   - But now tha I think about it, we'll use array because a dictionary is more
        #     memory heavy comapred to the same size of array
        # - Algorithm:
        #   - Create a new array called runningProducts which is an array of array of integers
        #     - e.g. runningProducts = [[1,3],[4,5]...]
        #     - Initialize it at runningProducts = []
        #   - Iterate through the array nums once from left to right and for each num:
        #     - Create an array of integers called product = []
        #     - If the currentIndex > 0:
        #       - product.append(product[currentIndex-1]*nums[currentIndex])
        #     - Else:
        #       - product.append(nums[currentIndex])
        #     - runningProducts.append(product)
        #   - Iterate through the array nums once from rigth to left and for each num:
        #     - If the currentIndex < (len(nums)-1):
        #       - runningProducts[currentIndex].append(nums[currentIndex]*product[currentIndex+1])
        #     - Else:
        #       - runningProducts[currentIndex].append(nums[currentIndex])
        #   - Create a new array of integers called output = []
        #   - Iterate through the runningProducts array from left to rigth and for each runningProduct:
        #     - leftProduct = (currentIndex>0)?runningProducts[currentIndex-1][0]:1
        #     - rightProduct = (currentIndex<(len(runningProducts)-1))?runningProducts[currentIndex+1][1]:1
        #     - output.append(leftProduct * rightProduct)
    
        bothProducts = [[1,1] for num in nums]
        for index,num in enumerate(nums):
            targetIndex = index
            leftProduct = bothProducts[targetIndex-1][0] if (targetIndex>0) else 1
            bothProducts[targetIndex][0] = (leftProduct * num) 
        for index,num in enumerate(nums[::-1]):
            targetIndex = -index-1
            rightProduct = bothProducts[targetIndex+1][1] if (index<len(nums)-1) else 1
            bothProducts[targetIndex][1] = (num * rightProduct) 
        output = []
        for index in range(0,len(bothProducts)):
            leftProduct = bothProducts[index-1][0] if (index>0) else 1
            rightProduct = bothProducts[index+1][1] if (index<len(bothProducts)-1) else 1
            output.append(leftProduct * rightProduct)
        return output
