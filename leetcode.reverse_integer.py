class Solution(object):
    def reverse(self, x):
        MAX = 2**31
        revers = 0
        isNegative = x < 0
        x = abs(x)
        while x:
            if revers > MAX // 10:
                return 0
            remainder = x % 10
            revers = (revers * 10) + remainder
            x = x // 10
        if isNegative:
            return -revers
        else:
            return revers



p = Solution()
x = 123
print(p.reverse(x))