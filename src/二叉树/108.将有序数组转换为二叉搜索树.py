class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):

        if len(nums) == 0:
            return None

        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid:])
        root.right = self.sortedArrayToBST(nums[mid+1::])

        return root


def printTree(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    while result and result[-1] is None:
        result.pop()

    return result


nums = [-10, -3, 0, 5, 9]

solution = Solution()
root = solution.sortedArrayToBST(nums)

print(printTree(root))