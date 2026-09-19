class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
# class Solution(object):
#     def inorderTraversal(self, root):
#         if root is None:
#             return []
#
#         leftResult = self.inorderTraversal(root.left)
#         rightResult = self.inorderTraversal(root.right)
#
#         return leftResult + [root.val] + rightResult


# 迭代
class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current is not None or stack:

            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result


TreeNode3 = TreeNode(3,None,None)
TreeNode2 = TreeNode(2,TreeNode3,None)
TreeNode1 = TreeNode(1,None,TreeNode2)

print(Solution().inorderTraversal(TreeNode1))