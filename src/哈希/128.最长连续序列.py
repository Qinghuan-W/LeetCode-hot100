class Solution(object):
    def longestConsecutive(self, nums):
        num_set=set(nums)
        longest=0
        for i in num_set:
            if i-1 not in num_set:
                current = i
                length = 1
                while current+1 in num_set:
                    current = current+1
                    length += 1
                longest = max(longest,length)

        return longest

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
