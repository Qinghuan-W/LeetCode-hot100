# class Solution(object):
#     def rotate(self, nums, k):
#         actualRotate = k % len(nums)
#         for i in range(actualRotate):
#             nums.insert(0,nums.pop())
#         return nums

class Solution(object):
    def rotate(self, nums, k):
        actualRotate = k % len(nums)

        nums[:] = nums[-actualRotate:] + nums[:-actualRotate]
        return nums

print(Solution().rotate([1,2,3,4,5,6,7,8,9], 3))