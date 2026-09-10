from unicodedata import digit


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        pointer1 = l1
        pointer2 = l2

        while pointer1 is not None or pointer2 is not None or carry != 0:

            if pointer1 is None:
                val1 = 0
            else:
                val1 = pointer1.val

            if pointer2 is None:
                val2 = 0
            else:
                val2 = pointer2.val

            sumOfpointer = val1 + val2 + carry

            digit = sumOfpointer % 10
            carry = sumOfpointer // 10

            tail.next = ListNode(digit)
            tail = tail.next

            if pointer1 is not None:
                pointer1 = pointer1.next

            if pointer2 is not None:
                pointer2 = pointer2.next

        return dummy.next










# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         num1Arr = []
#         num2Arr = []
#
#         pointer1 = l1
#         pointer2 = l2
#
#         while pointer1 is not None:
#             num1Arr.append(pointer1.val)
#             pointer1 = pointer1.next
#
#         while pointer2 is not None:
#             num2Arr.append(pointer2.val)
#             pointer2 = pointer2.next
#
#         num1Arr.reverse()
#         num2Arr.reverse()
#
#         num1 = 0
#         num2 = 0
#
#         for x in num1Arr:
#             num1 = num1 * 10 + x
#
#         for x in num2Arr:
#             num2 = num2 * 10 + x
#
#         resultNum = num1 + num2
#
#         if resultNum == 0:
#             return ListNode(0)
#
#         dummy = ListNode(0)
#         tail = dummy
#
#         while resultNum > 0:
#             digit = resultNum % 10
#
#             tail.next = ListNode(digit)
#             tail = tail.next
#
#             resultNum //= 10
#
#         return dummy.next


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

result = Solution().addTwoNumbers(node1, node4)
