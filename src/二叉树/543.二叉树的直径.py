class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):

        self.diameter = 0
        self.maxDepth(root)

        return self.diameter


    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)

        currentDiameter = leftDepth +rightDepth
        self.diameter = max(self.diameter,currentDiameter)

        return 1 + max(leftDepth, rightDepth)




TreeNode1 = TreeNode(1)
TreeNode2 = TreeNode(2)
TreeNode3 = TreeNode(3)
TreeNode4 = TreeNode(4)
TreeNode5 = TreeNode(5)

TreeNode1.left = TreeNode2
TreeNode1.right = TreeNode3
TreeNode2.left = TreeNode4
TreeNode2.right = TreeNode5

print(Solution().diameterOfBinaryTree(TreeNode1))