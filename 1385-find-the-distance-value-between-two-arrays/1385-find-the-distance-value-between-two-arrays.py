class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count=0
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    count+=1
                    break
        return len(arr1)-count