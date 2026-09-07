class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        newHead = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return newHead




# iterative
# class Solution(object):
#     def reverseList(self, head):
#         previous = None
#         current = head
#
#         while current != None:
#             nextNode = current.next
#
#             current.next = previous
#
#             previous = current
#             current = nextNode
#
#         return previous





# iterative
# class Solution(object):
#     def reverseList(self, head):
#
#         NodeNumber = 0
#         currentcountNode = head
#         while currentcountNode != None:
#             NodeNumber += 1
#             currentcountNode = currentcountNode.next
#
#         newHead = head
#         for i in range(NodeNumber - 1):
#             newHead = newHead.next
#
#
#         newTail  = newHead
#
#         OperateNumber = NodeNumber-1
#         while OperateNumber > 0:
#
#             currentNode = head
#             for i in range(OperateNumber-1):
#                 currentNode =currentNode.next
#
#             newTail.next = currentNode
#             currentNode.next = None
#             newTail = currentNode
#             OperateNumber -= 1
#
#         return newHead







node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1


# 测试
print(Solution().reverseList(head))