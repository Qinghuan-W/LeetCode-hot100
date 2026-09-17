from wtforms.validators import length


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        length = 0
        current = head

        while current is not None:
            length += 1
            current = current.next

        leftSize = length //2
        current = head

        for i in range(leftSize - 1):
            current = current.next

        rightHead = current.next
        current.next = None

        left = self.sortList(head)
        right =self.sortList(rightHead)

        dummy = ListNode(0)
        tail = dummy

        while left is not None and right is not None:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right =right.next

            tail = tail.next

        if left is not None:
            tail.next = left
        else:
            tail.next = right

        return dummy.next



