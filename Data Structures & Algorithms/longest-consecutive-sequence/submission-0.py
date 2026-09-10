class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbersSet=set(nums)
        longest=0

        for num in nums:
            if (num-1) not in numbersSet:
                length = 1
                while (num+length) in numbersSet:
                    length+=1
                longest = max(length,longest)
        return longest