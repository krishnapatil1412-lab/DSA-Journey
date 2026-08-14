class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = sum(nums[:k])
        maxAvg = ans / k

        for i in range(1, len(nums) - k + 1):
            ans = ans - nums[i - 1] + nums[i + k - 1]
            maxAvg = max(maxAvg, ans / k)

        return maxAvg
        