class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmapS={}
        hmapT={}
        for i in s:
            if i in hmapS:
                hmapS[i]+=hmapS[i]
            else:
                hmapS[i]=1
        
        for j in t:
            if j in hmapT:
                hmapT[j]+=hmapT[j]
            else:
                hmapT[j]=1
        
        if hmapS==hmapT:
            return True
        else:
            return False
        