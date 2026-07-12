class Solution(object):
    def isValid(self, s):
        st='([{'
        l=[]
        for i in s:
            if i in st:
                l.append(i)
            elif(len(l)!=0):
                top=l.pop()
                if(i==")" and top=="("):
                    continue
                elif(i=="]" and top=="["):
                    continue
                elif(i=="}" and top=="{"):
                    continue
                else:
                    return False
                    break
            else:
                return False
                break
        return len(l)==0