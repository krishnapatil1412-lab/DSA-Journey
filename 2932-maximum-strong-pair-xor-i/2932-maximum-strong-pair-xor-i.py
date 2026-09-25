class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        return max((x^y for x, y in 
                     filter(lambda x: x[0] <= x[1] <= 2*x[0],
                       permutations(nums, 2))), default = 0)