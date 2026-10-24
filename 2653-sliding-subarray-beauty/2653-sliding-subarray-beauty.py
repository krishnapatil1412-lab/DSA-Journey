class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        sl, ans = SortedList(), []
        for i, y in enumerate(nums):
            sl.add(y)
            if len(sl) > k: sl.remove(nums[i - k])
            if i >= k - 1: ans.append(min(0, sl[x - 1]))
        return ans