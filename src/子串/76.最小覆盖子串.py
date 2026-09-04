class Solution(object):
    def minWindow(self, s, t):
        tCount = {}

        for ch in t:
            tCount[ch] = tCount.get(ch, 0) + 1

        windowCount = {}

        required = len(tCount)
        formed = 0

        left = 0

        minLength = float('inf')
        minLeft = 0
        minRight = 0

        for right in range(len(s)):
            ch = s[right]

            windowCount[ch] = windowCount.get(ch, 0) + 1

            if ch in tCount and windowCount[ch] == tCount[ch]:
                formed += 1

            while formed == required:
                currentLength = right - left + 1

                if currentLength < minLength:
                    minLength = currentLength
                    minLeft = left
                    minRight = right

                leftChar = s[left]
                windowCount[leftChar] -= 1

                if leftChar in tCount and windowCount[leftChar] < tCount[leftChar]:
                    formed -= 1

                left += 1

        if minLength == float('inf'):
            return ""

        return s[minLeft:minRight + 1]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))