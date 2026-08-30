class Solution(object):
    def flipAndInvertImage(self, image):
        return [[1 ^ i for i in reversed(row)] for row in image]
