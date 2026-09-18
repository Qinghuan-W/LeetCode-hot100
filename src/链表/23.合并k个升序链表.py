class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            newLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]

                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                merged = self.mergeTwoLists(l1, l2)
                newLists.append(merged)

            lists = newLists

        return lists[0]


    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1 is not None:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next


# 暴力解法
# class Solution(object):
#     def mergeKLists(self, lists):
#         if not lists:
#             return None
#
#         dummy = ListNode(0)
#         tail = dummy
#
#
#         while True:
#             position = -1
#             minNum = float('inf')
#
#             for i in range(len(lists)):
#                 if lists[i] is not None:
#                     if lists[i].val <= minNum:
#                         minNum = lists[i].val
#                         position = i
#
#             if position == -1:
#                 break
#
#             tail.next = lists[position]
#             tail = tail.next
#             lists[position] = lists[position].next
#
#         return dummy.next

node1 = ListNode(1)
node2 = ListNode(4)
node3 = ListNode(5)

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node7 = ListNode(2)
node8 = ListNode(6)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

node7.next = node8

lists = [node1, node4, node7]

result = Solution().mergeKLists(lists)

current = result
while current is not None:
    print(current.val,end="->")
    current = current.next

print("None")



