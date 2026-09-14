class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        nodeLeftCount = 0
        currentNode = head

        while currentNode is not None:
            nodeLeftCount += 1
            currentNode = currentNode.next

        currentNode = head
        previousTail = None

        while nodeLeftCount >= k:
            newTail = currentNode
            newHead = currentNode


            for i in range(k - 1):
                nextNode = newTail.next

                newTail.next = nextNode.next
                nextNode.next = newHead
                newHead = nextNode

            if previousTail is None:
                head = newHead
            else:
                previousTail.next = newHead

            previousTail = newTail

            currentNode = newTail.next

            nodeLeftCount -= k


        return head







