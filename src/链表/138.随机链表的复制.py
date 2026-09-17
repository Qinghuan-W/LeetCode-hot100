class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        mapping = {None: None}
        current = head

        while current is not None:
            newNode = Node(current.val)
            mapping[current] = newNode
            current = current.next

        current = head

        while current is not None:
            newNode = mapping[current]
            newNode.next = mapping[current.next]
            newNode.random = mapping[current.random]
            current = current.next

        return mapping[head]