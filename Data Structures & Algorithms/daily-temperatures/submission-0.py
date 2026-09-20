class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        stack = [] #index,temperature pairs 

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
               StackI,StackT=stack.pop()
               res[StackI]=i-StackI
            stack.append((i,t))
        return res
