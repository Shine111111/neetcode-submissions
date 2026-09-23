class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        positionMap = {}
        l=0
        res = 0

        for r in range(len(s)):
            if s[r] in positionMap:
                l = max(l, positionMap[s[r]]+1)
            positionMap[s[r]]=r
            res = max(res, r-l+1)
        return res