class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        res = []
        r = 0 
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                l = max(r, j - k)
                r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    res.append(i)
        return res