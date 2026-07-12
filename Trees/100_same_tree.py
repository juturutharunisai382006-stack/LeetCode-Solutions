class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif q is None and p is not None:
            return False
        if(p.val==q.val):
            l=self.isSameTree(p.left,q.left)
            r=self.isSameTree(p.right,q.right)
            return l and r
        else:
            return False
