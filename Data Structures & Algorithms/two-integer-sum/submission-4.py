class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i in range(len(nums)):

            difference = target - nums[i]

            if difference in diffs:
                return [diffs[difference], i]
            else:
                diffs[nums[i]]=i
                