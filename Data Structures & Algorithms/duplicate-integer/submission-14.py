class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            nums_set.add(nums[i])
        if len(nums) != len(nums_set): 
            return True
        else: 
            return False
