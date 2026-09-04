# class Solution(object):
#     def productExceptSelf(self, nums):
#         n = len(nums)
#
#         left = [1] * n
#         right = [1] * n
#         answer = [1] * n
#
#         for i in range(1, n):
#             left[i] = nums[i - 1] * left[i - 1]
#
#         for i in range(n - 2, -1, -1):
#             right[i] = right[i + 1] * nums[i + 1]
#
#         for i in range(n):
#             answer[i] = left[i] * right[i]
#
#         return answer
#

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        right = 1

        for i in range(n - 1, -1, -1):
            answer[i] = answer[i] * right
            right = right * nums[i]

        return answer