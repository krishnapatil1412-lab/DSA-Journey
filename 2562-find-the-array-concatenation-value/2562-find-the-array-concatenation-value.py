class Solution(object):
    def findTheArrayConcVal(self, nums):
        l=len(nums)-1
        if l==0:
            return 1
        v=0
        for i in range(l):
            if l-i==i:
                v+=nums[i]
                break
            elif l-i <i:
                break
            else:
                v+=int(str(nums[i])+str(nums[l-i]))
        return v