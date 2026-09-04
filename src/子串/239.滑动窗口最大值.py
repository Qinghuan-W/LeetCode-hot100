# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         leftPointer = 0
#         rightPointer = leftPointer+k-1
#         maxNumberArray = []
#
#         while rightPointer < len(nums):
#             newArray = nums[leftPointer:rightPointer+1]
#             maxNow = max(newArray)
#
#             maxNumberArray.append(maxNow)
#             leftPointer +=1
#             rightPointer +=1
#         return maxNumberArray
#
# print(Solution().maxSlidingWindow([1,-1],1))


from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        queue = deque()
        result = []

        for right in range(len(nums)):

            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)

            left = right - k + 1

            if queue[0] < left:
                queue.popleft()

            if right >= k - 1:
                result.append(nums[queue[0]])

        return result

print(Solution().maxSlidingWindow([1,-1],1))