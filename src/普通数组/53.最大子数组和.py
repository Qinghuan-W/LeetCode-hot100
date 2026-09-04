# class Solution(object):
#     def maxSubArray(self, nums):
#         maxSum = float('-inf')
#
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 currentSum = sum(nums[i:j + 1])
#                 maxSum = max(maxSum, currentSum)
#
#         return maxSum
#


class Solution(object):
    def maxSubArray(self, nums):

        sumArray = float('-inf')
        maxSum = float('-inf')
        array = []
        for i in nums:
            if i > i + sumArray:
                sumArray = i
            else:
                sumArray += i
            maxSum = max(maxSum, sumArray)

        return maxSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
