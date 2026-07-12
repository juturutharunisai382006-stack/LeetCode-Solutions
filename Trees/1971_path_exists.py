from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True
        d={}
        for u,v in edges:
            if u not in d:
                d[u]=[]
            if v not in d:
                d[v]=[]
            d[u].append(v)
            d[v].append(u)
        v=set([source])
        q=deque()
        q.append(source)
        while q:
            f=q.popleft()
            if f == destination :
                return True
            for i in d.get(f,[]):
                if i not in v:
                    q.append(i)
                    v.add(i)
        return False
