class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 双指针
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         dummy = ListNode(0)
#         dummy.next = head
#
#         left = dummy
#         right = dummy
#
#         for i in range(n + 1):
#             right = right.next
#
#         while right is not None:
#             left = left.next
#             right = right.next
#
#         left.next = left.next.next
#
#         return dummy.next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        currentCountNode = head
        nodeNumber = 0

        while currentCountNode is not None:
            nodeNumber += 1
            currentCountNode = currentCountNode.next

        deleteIndex = nodeNumber - n
        currentIndex = 0
        currentNode = head
        previous = None

        if nodeNumber == 1:
            return None
        for i in range(0,deleteIndex+1):
            if currentIndex != deleteIndex:
                currentIndex += 1
                previous = currentNode
                currentNode = currentNode.next
            else:
                if currentNode.next is None:
                    previous.next = None
                if nodeNumber == n:
                    head = head.next
                else:
                    previous.next = currentNode.next

        return head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

newHead = Solution().removeNthFromEnd(node1, 2)

currentNode = newHead

while currentNode is not None:
    print(currentNode.val)
    currentNode = currentNode.next




