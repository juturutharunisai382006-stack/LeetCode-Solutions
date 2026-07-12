class Solution(object):
    def minDepth(self, root):
        return self.mini(root)
    def mini(self,node):
        if node is None:
            return 0
        elif node.left is None:
            return 1+self.mini(node.right)
        elif node.right is None:
            return 1+self.mini(node.left)
        l=self.mini(node.left)
        r=self.mini(node.right)
        return 1 + min(l,r)