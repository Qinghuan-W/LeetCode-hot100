class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def isPalindrome(self, head):

        nodeNumber = 0
        currentCountNode = head

        while currentCountNode != None:
            nodeNumber += 1
            currentCountNode = currentCountNode.next

        # 反转前半部分
        previous = None
        currentNode = head

        for i in range(nodeNumber // 2):
            nextNode = currentNode.next

            currentNode.next = previous

            previous = currentNode
            currentNode = nextNode

        if nodeNumber % 2 == 0:
            leftPointer = previous
            rightPointer = currentNode

        else:
            leftPointer = previous
            rightPointer = currentNode.next

        while leftPointer != None:
            if leftPointer.val != rightPointer.val:
                return False

            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        return True



# class Solution(object):
#     def isPalindrome(self, head):
#         values = []
#
#         currentNode = head
#         while currentNode != None:
#             values.append(currentNode.val)
#             currentNode = currentNode.next
#
#         return values[::] == values[::-1]


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

print(Solution().isPalindrome(node1))