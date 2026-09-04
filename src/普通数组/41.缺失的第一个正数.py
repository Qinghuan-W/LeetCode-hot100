# class Solution(object):
#     def firstMissingPositive(self, nums):
#         nums.sort()
#         if 1 not in nums:
#             return 1
#         else:
#             for i in range(len(nums)-1):
#                 if nums[i+1]-nums[i] > 1 and nums[i]>0:
#                     return nums[i] +1
#                 else:
#                     continue
#             return nums[len(nums)-1]+1

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correctIndex = nums[i] - 1
                nums[i], nums[correctIndex] = nums[correctIndex], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
print(Solution().firstMissingPositive([1,1000]))