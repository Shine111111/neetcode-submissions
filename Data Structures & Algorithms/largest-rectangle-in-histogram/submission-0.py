class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i #we haven't extending it back yet
            while stack and stack[-1][1] > h:
                index, height = stack.pop() # now that the height is great we should go back to the biggest
                area = max(area, height*(i - index))
                start = index
            stack.append((start,h)) # now the start of is at the top of the stack

        for i , h in stack:
            area= max(area, h*(len(heights)-i)) # cases that stayed at the end 
        return area