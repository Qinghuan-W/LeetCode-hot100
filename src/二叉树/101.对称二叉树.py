class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
# class Solution(object):
#     def isSymmetric(self, root):
#         if root is None:
#             return True
#         else:
#             return self.check(root.left,root.right)
#
#
#
#     def check(self,node1,node2):
#         if node1 is None and node2 is None:
#             return True
#         if node1 is None and node2 is not None:
#             return False
#         if node1 is not None and node2 is None:
#             return False
#         if node1 is not None and node2 is not None and node2.val != node1.val:
#             return False
#
#         return self.check(node1.left,node2.right) and self.check(node1.right,node2.left)



class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True

        stack = [(root.left, root.right)]

        while stack:
            node1, node2 = stack.pop()

            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False

            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))

        return True