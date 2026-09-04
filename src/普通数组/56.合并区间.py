class Solution(object):
    def merge(self, intervals):
        intervals.sort()

        current = intervals[0]
        result = []

        for i in range(0, len(intervals) - 1):

            if current[1] >= intervals[i + 1][0]:

                if current[1] >= intervals[i + 1][1]:
                    current = [current[0], current[1]]
                else:
                    current = [current[0], intervals[i + 1][1]]

            else:
                result.append(current)
                current = [intervals[i + 1][0], intervals[i + 1][1]]

        result.append(current)

        return result

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))