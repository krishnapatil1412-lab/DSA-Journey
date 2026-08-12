class Solution(object):
    def reverseOnlyLetters(self, s):
        letters = []

        for c in s:
            if c.isalpha():
                letters.append(c)

        letters.reverse()

        result = list(s)
        index = 0

        for i in range(len(result)):
            if result[i].isalpha():
                result[i] = letters[index]
                index += 1

        return ''.join(result)