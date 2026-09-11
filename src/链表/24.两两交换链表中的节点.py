class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        trigger = 0
        previous = None
        currentNode = head
        previousPairTail = None

        while currentNode is not None:
            trigger +=1
            nextNode = currentNode.next

            if trigger == 1:
                previous = currentNode
                currentNode = nextNode
            elif trigger == 2:
                currentNode.next = previous
                previous.next = nextNode

                if previousPairTail is None:
                    head = currentNode
                else:
                    previousPairTail.next = currentNode

                previousPairTail = previous

                currentNode = nextNode
                trigger = 0

        return head

class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        previous = dummy

        while previous.next is not None and previous.next.next is not None:
            first = previous.next
            second = first.next

            first.next = second.next
            second.next = first
            previous.next = second

            previous = first

        return dummy.next