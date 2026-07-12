class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        r=1
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        w=s[l:r]
        c=1
        maxi=1
        while r!=len(s):
            if s[r] not in w:
                w+=s[r]
                c+=1
                maxi=max(c,maxi)
                r+=1
            else:
                w=s[l+1:r]
                c-=1
                l+=1
        return maxi