from unittest import skip


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        currentPointer1 = list1
        currentPointer2 = list2

        if currentPointer1 is None:
            return currentPointer2
        elif currentPointer2 is None:
            return currentPointer1

        dummy = ListNode(0)
        tail = dummy

        while currentPointer1 is not None and currentPointer2 is not None:
            if currentPointer1.val <= currentPointer2.val:
                tail.next = currentPointer1
                tail = tail.next
                currentPointer1 = currentPointer1.next
                continue
            if currentPointer2.val <= currentPointer1.val:
                tail.next = currentPointer2
                tail = tail.next
                currentPointer2 = currentPointer2.next

        if currentPointer1 is None:
            tail.next = currentPointer2
        elif currentPointer2 is None:
            tail.next = currentPointer1

        return dummy.next






node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

Solution().mergeTwoLists(node1,node4)