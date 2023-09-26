class EmptyInputDataException(Exception):
    def __init__(self, message: str = 'Input data empty'):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class Solution(object):
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            raise EmptyInputDataException()


        output = strs[0]
        for i in range(1, len(strs)):
            temp = ""
            if len(output) == 0:
                break
            for j in range(len(strs[i])):
                if j <len(output) and output[j] == strs[i][j]:
                    temp += output[j]
                else:
                    break
            output = temp
        return output

p = Solution()
strs = []
print(p.longestCommonPrefix(strs))
