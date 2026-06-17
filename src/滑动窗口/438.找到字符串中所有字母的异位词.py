#暴力解法
# class Solution(object):
#     def findAnagrams(self, s, p):
#         lenOfObject = len(p)
#         result = []
#         sortedP = sorted(p)
#
#         for i in range(len(s) - lenOfObject + 1):
#             substring = s[i:i + lenOfObject]
#
#             if sorted(substring) == sortedP:
#                 result.append(i)
#         return result

class Solution(object):
    def findAnagrams(self, s, p):
        result = []

        lenP = len(p)

        pCount = {}
        windowCount = {}

        for ch in p:
            pCount[ch] = pCount.get(ch, 0) + 1

        for right in range(len(s)):
            ch = s[right]
            windowCount[ch] = windowCount.get(ch, 0) + 1

            if right >= lenP:
                leftChar = s[right - lenP]
                windowCount[leftChar] -= 1

                if windowCount[leftChar] == 0:
                    del windowCount[leftChar]

            if windowCount == pCount:
                result.append(right - lenP + 1)

        return result

print(Solution().findAnagrams("cbaebabacd","abc"))