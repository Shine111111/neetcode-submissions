class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        parsed = set()


        for n in nums:
            if n in parsed:
                return True
            else:
                parsed.add(n)
        return False