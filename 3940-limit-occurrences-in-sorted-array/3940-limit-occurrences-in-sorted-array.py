class Solution(object):
    def limitOccurrences(self, nums, k):
        n = len(nums)
        j = 1
        count = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= k:
                nums[j] = nums[i]
                j += 1

        ans = [0] * j

        for i in range(j):
            ans[i] = nums[i]

        return ans
        