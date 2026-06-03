#暴力解法：
#
# class Solution:
#     def groupAnagrams(self, strs):
#
#         result = []
#         used = set()
#
#         for i in range(len(strs)):
#
#             if i in used:
#                 continue
#
#             group = [strs[i]]
#             used.add(i)
#
#             for j in range(i + 1, len(strs)):
#
#                 if j not in used and sorted(strs[i]) == sorted(strs[j]):
#                     group.append(strs[j])
#                     used.add(j)
#
#             result.append(group)
#
#         return result
#
#字典
class Solution:
    def groupAnagrams(self, strs):

        groups = {}

        for s in strs:

            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())