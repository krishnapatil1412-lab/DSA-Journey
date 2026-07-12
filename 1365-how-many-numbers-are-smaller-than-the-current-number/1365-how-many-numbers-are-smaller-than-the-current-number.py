class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        countList=[0]*(101)
        for num in nums:
            countList[num]+=1
        output = []
        for num in nums:
            output.append(sum(countList[:num]))
        return output 