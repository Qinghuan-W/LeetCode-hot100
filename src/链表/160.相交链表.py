class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        Acount =0
        Bcount =0

        currentCountA = headA
        currentCountB = headB

        if headA is not None:
            Acount = 1

        if headB is not None:
            Bcount = 1

        while currentCountA.next != None:
            Acount += 1
            currentCountA = currentCountA.next

        while currentCountB.next != None:
            Bcount += 1
            currentCountB = currentCountB.next

        if Acount < Bcount:
            diff = Bcount - Acount
            for i in range(diff):
                headB = headB.next

            currentA = headA
            currentB = headB
            for i in range(Bcount-diff):
                if currentA == currentB:
                    return currentA
                else:
                    currentA = currentA.next
                    currentB = currentB.next


        if Acount > Bcount:
            diff = Acount - Bcount
            for i in range(diff):
                headA = headA.next

            currentA = headA
            currentB = headB
            for i in range(Acount - diff):
                if currentA == currentB:
                    return currentA
                else:
                    currentA = currentA.next
                    currentB = currentB.next


        if Acount == Bcount:
            currentA = headA
            currentB = headB
            for i in range(Acount):
                if currentA == currentB:
                    return currentA
                else:
                    currentA = currentA.next
                    currentB = currentB.next






# 公共部分：4 -> 5 -> 4
common = ListNode(4)
common.next = ListNode(5)
common.next.next = ListNode(4)

# A: 2 -> 2 -> 4 -> 5 -> 4
headA = ListNode(2)
headA.next = ListNode(2)
headA.next.next = common

# B: 2 -> 2 -> 4 -> 5 -> 4
headB = ListNode(2)
headB.next = ListNode(2)
headB.next.next = common


result = Solution().getIntersectionNode(headA, headB)

if result:
    print("Intersected at:", result.val)
else:
    print("No intersection")