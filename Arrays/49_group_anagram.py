class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            s=i
            s = ''.join(sorted(s))
            if(s not in d):
                d[s]=[i]
            else:
                d[s]=d.get(s) + [i]
        return list(d.values())