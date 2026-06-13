#暴力解法
# class Solution:
#     def maxArea(self, height):
#         maxValue = 0
#         for i in range(0,len(height)):
#             for j in range(i+1,len(height)):
#                 if min(height[i],height[j])*(j-i) > maxValue:
#                     maxValue=min(height[i],height[j])*(j-i)
#                 else:
#                     continue
#         return maxValue

class Solution:
    def maxArea(self, height):
        maxValue = 0
        Lpointer = 0
        Rpointer = len(height)-1
        while Lpointer != Rpointer:
            Value = min(height[Lpointer],height[Rpointer]) * (Rpointer - Lpointer)
            if Value > maxValue:
                maxValue = Value
            if height[Lpointer] < height[Rpointer]:
                Lpointer += 1
            else:
                Rpointer -= 1
        return maxValue


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))