class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.split()
        l=len(words[-1])
        return l