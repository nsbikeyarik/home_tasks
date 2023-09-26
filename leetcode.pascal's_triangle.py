class Solution(object):
    def generate(self, numRows):
        result= [[1]]
        for i in range(numRows-1):
            temp = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(temp[j]+ temp[j +1])
            result.append(row)
        return result




p = Solution()
numRows = 4
print(p.generate(numRows))


class ValidationError(Exception):
    def __init__(self, message, errors):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors


class ValidateMethodException(Exception):
    def __init__(self, message, input_data):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.input_data = input_data



def some_example(method):
    try:
        if method not in ('LogIn', 'LogOff'):
            raise ValidateMethodException('Method not found', method)
    except ValidateMethodException as exception:
        print(exception.input_data)
        print(exception)


if __name__ == '__main__':
    some_example('7638295623795629')


