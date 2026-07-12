class Solution(object):
    def findCenter(self, edges):
        d={}
        for u,v in edges:
            if u not in d:
                d[u]=[]
            if v not in d:
                d[v]=[]
            d[u].append(v)
            d[v].append(u)
        n=len(d)
        for k,v in d.items():
            if len(v) == n-1:
                return k