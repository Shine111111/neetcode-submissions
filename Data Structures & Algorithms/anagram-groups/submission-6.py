class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            letter_freq=[0]*26
            for c in s:
                letter_freq[ord(c)-ord("a")]+=1
            res[tuple(letter_freq)].append(s)
        return list(res.values())
                