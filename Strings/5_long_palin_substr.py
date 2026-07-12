class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==0:
            return ""
        if len(s)==1:
            return s[0]
        start=0
        maxlen=1
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    start = l
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > maxlen:
                    maxlen = r-l+1
                    start = l
                l-=1
                r+=1
        return s[start:start + maxlen]