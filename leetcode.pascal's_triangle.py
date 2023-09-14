class Solution(object):
    def generate(self, numRows):
        numRows = numRows
        output = []
        if numRows == 0:
            return []
        if numRows == 1:
            return [1]

p = Solution()
numRows = 1
print(p.generate(numRows))




