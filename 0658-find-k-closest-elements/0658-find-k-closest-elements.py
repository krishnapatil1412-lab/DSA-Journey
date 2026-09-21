class Solution:
    def findClosestElements(self, arr, k, x):

        li = []

        for i in range(k):
            li.append(arr[i])

        for i in range(k, len(arr)):

            if abs(arr[i - k] - x) > abs(arr[i] - x):
                li.remove(arr[i - k])
                li.append(arr[i])

        return li