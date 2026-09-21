class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        finalresult = []
        queue = [root]

        while queue:
            levelSize = len(queue)
            result = []
            nextQueue = []

            for i in range(levelSize):
                currentNode = queue[i]
                result.append(currentNode.val)

                if currentNode.left is not None:
                    nextQueue.append(currentNode.left)
                if currentNode.right is not None:
                    nextQueue.append(currentNode.right)

            finalresult.append(result)

            queue = nextQueue
        return finalresult

