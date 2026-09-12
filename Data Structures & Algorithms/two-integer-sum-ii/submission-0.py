class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right :
            currentSum=numbers[left]+numbers[right] # better than checking if the right is bigger than target 

            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left+1, right+1] # becasue the output needs to be 1 indexed 
        return []
