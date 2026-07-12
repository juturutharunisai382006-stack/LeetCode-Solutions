class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        l=self.countNodes(root.left)
        r=self.countNodes(root.right)
        return 1+l+r
        