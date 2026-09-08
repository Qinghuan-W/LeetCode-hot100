class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def hasCycle(self,head):
        slowPointer = head
        fastPointer = head

        while slowPointer is not None:
            if fastPointer is not None and fastPointer.next is not None:
                fastPointer = fastPointer.next.next
                slowPointer = slowPointer.next
                if fastPointer == slowPointer:
                    return True
            else:
                return False


        return False


#字典方法
# class Solution(object):
#     def hasCycle(self, head):
#         visited = {}
#         currentNode = head
#
#         while currentNode is not None:
#
#             if currentNode not in visited:
#                 visited[currentNode] = 1
#             else:
#                 visited[currentNode] += 1
#
#             if visited[currentNode] >= 2:
#                 return True
#
#             currentNode = currentNode.next
#
#         return False

#SET方法
# class Solution(object):
#     def hasCycle(self, head):
#         visited = set()
#         currentNode = head
#         while currentNode != None:
#             if currentNode.next is None:
#                 return False
#             else:
#                 if currentNode not in visited:
#                     visited.add(currentNode)
#                     currentNode = currentNode.next
#                 else:
#                     return True

# node1 = ListNode(3)
# node2 = ListNode(2)
# node3 = ListNode(0)
# node4 = ListNode(-4)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2



node1 = ListNode(1)
# node2 = ListNode(2)
# node1.next = node2
print(Solution().hasCycle(node1))