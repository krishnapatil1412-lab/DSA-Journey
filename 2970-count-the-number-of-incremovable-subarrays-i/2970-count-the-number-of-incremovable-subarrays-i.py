class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count, n = 0, len(nums)
        for start in range(n):
            for end in range(start, n):
                if self.isIncremovable(nums, start, end):
                    count += 1
        return count

    def isIncremovable(self, nums: List[int], start: int, end: int) -> bool:
        last = -(2**31)
        for i in range(start):
            if nums[i] <= last:
                return False
            last = nums[i]
        for i in range(end + 1, len(nums)):
            if nums[i] <= last:
                return False
            last = nums[i]
        return True