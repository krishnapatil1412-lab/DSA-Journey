class Solution(object):
    def maxChunksToSorted(self, arr):
        chunk_count = 0
        prefix_max = float('-inf')   
        length = len(arr)

        suffix_min = [0] * length
        suffix_min[length - 1] = float('inf') 

        for i in range(length - 2, -1, -1):
            suffix_min[i] = min(arr[i + 1], suffix_min[i + 1])

        for i in range(length):
            prefix_max = max(arr[i], prefix_max)

            if suffix_min[i] > prefix_max:
                chunk_count += 1

        return chunk_count