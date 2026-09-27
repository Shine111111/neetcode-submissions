class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        q = deque() #chose deque to be able to add and remove from left AND right

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # if i hve smaller values than the current in nums
                q.pop()
            q.append(r) #just push the index of the value


            if l > q[0]:
                q.popleft()

            if (r+1)>=k:
                res.append(nums[q[0]])
                l += 1

            r+=1
        return res