from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        # d={}
        # for i in range(len(rooms)):
        #     d[i]=rooms[i]
        q=deque()
        v=set([0])
        q.append(0)
        while q:
            t=q.popleft()
            for i in rooms[t]:
                if i not in v:
                    q.append(i)
                    v.add(i)
        if len(v)==len(rooms):
            return True
        return False