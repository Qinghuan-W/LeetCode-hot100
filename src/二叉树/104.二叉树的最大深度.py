class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)

        return 1+max(leftDepth,rightDepth)


TreeNode1 = TreeNode(3)
TreeNode2 = TreeNode(9)
TreeNode3 = TreeNode(20)
TreeNode4 = TreeNode(15)
TreeNode5 = TreeNode(7)

TreeNode1.left = TreeNode2
TreeNode1.right = TreeNode3
TreeNode3.left = TreeNode4
TreeNode3.right = TreeNode5

print(Solution().maxDepth(TreeNode1))



