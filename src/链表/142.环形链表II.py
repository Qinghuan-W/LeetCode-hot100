from asyncio.windows_events import NULL

from sqlalchemy import null


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        slowPointer = head
        fastPointer = head

        while slowPointer is not None:
            if fastPointer is not None and fastPointer.next is not None:
                fastPointer = fastPointer.next.next
                slowPointer = slowPointer.next

                if fastPointer == slowPointer:
                    headPointer = head
                    meetPointer = slowPointer

                    while headPointer != meetPointer:
                        headPointer = headPointer.next
                        meetPointer = meetPointer.next

                    return headPointer

            else:
                return None

        return None



node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(Solution().detectCycle(node1))