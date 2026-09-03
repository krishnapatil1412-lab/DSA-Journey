class Solution(object):
    def rearrangeString(self, s, x, y):
        return "".join(sorted(s, reverse=y > x))