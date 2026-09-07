class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))+"@"+s
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0

        while start < len(s):
            end = start #kinda regretting the variable names i chose
            while s[end] != "@":
                end +=1
            length = int(s[start:end])
            res.append(s[end+1 : end+1+length])#starting after @ until we reached the end of the string with the string length
            start = end + 1 + length # we need the start for the new word
        return res

