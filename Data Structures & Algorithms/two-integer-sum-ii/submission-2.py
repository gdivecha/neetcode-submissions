class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # - Let's try to figure out the desired behavior given the context that it is supposed to be a 2-pointer question:
        #   - e.g. numbers = [1,2,3,4], target = 3
        #     - @ i=0,j=3 -> 1 and 4 -> Is (4+1)==(target=3)? No -> sum is greater -> j = j-1 = 2
        #     - @ i=0,j=2 -> 1 and 3 -> Is (3+1)==(target=3)? No -> sum is greater -> j = j-1 = 1
        #     - @ i=0,j=1 -> 1 and 2 -> Is (2+1)==(target=3)? Yes -> Return [1,2]
        #   - Let's try another e.g.[1,5,6,8,9,11,14], target = 17
        #     - @ i=0,j=6 -> 1 and 14 -> Is (14+1)==(target=17)? No -> sum is smaller -> i = i+1 = 1
        #     - @ i=1,j=6 -> 5 and 14 -> Is (14+5)==(target==17)? No -> sum is greater -> j = j-1 = 5
        #     - @ i=1,j=5 -> 5 and 11 -> Is (11+5)==(target==17)? No -> sum is smaller -> i = i+1 = 2
        #     - @ i=2,j=5 -> 6 and 11 -> Is (11+6)==(target==17)? Yes -> Return [1,2]

        # Algorithm:
        # - i = 0
        # - j = len(numbers)-1
        # - indicesForTargetSum = [i,j]
        # - While i<j:
        #   - currentSum = numbers[i]+numbers[j]
        #   - If currentSum == target:
        #     - return indicesForTargetSum
        #   - Else if currentSum > target:
        #     - j=j-1
        #   - Else if currentSum < target:
        #     - i=i+1

        i = 0
        j = len(numbers)-1
        indicesForTargetSum = [i+1,j+1]
        while i<j:
            currentSum = numbers[i] + numbers[j]
            print(currentSum)
            if currentSum == target:
                indicesForTargetSum = [i+1,j+1]
                break
            elif currentSum > target:
                j-=1
            elif currentSum < target:
                i+=1
        return indicesForTargetSum