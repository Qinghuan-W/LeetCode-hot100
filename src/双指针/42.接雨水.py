class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        leftMax = 0
        rightMax = 0

        water = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax:
                water += leftMax - height[left]
                left += 1
            else:
                water += rightMax - height[right]
                right -= 1
        return water

print(Solution().trap([4,2,0,3,2,5]))