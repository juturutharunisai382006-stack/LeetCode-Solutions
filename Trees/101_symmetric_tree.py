class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.mirror(root.left , root.right)
    def mirror(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val==right.val:        
            l=self.mirror(left.left,right.right)
            r=self.mirror(left.right,right.left)
            return l and r
        return False