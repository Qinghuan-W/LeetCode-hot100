#暴力解法
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         maxLength = 0
#
#         for i in range(len(s)):
#             substring = []
#
#             for j in range(i, len(s)):
#                 if s[j] in substring:
#                     break
#                 else:
#                     substring.append(s[j])
#                     maxLength = max(maxLength, len(substring))
#         return maxLength

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        leftPointer = 0
        rightPointer = 0
        maxlength = 0

        char = set()

        for rightPointer in range(len(s)):
            while s[rightPointer] in char:
                char.remove(s[leftPointer])
                leftPointer += 1
            char.add(s[rightPointer])

            maxlength = max(maxlength, rightPointer - leftPointer + 1)

        return maxlength


print(Solution().lengthOfLongestSubstring("abcabcbb"))