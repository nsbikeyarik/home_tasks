class Solution(object):
    def isPalindrome(self, x):
        num = x
        temp = num
        reverse = 0
        while temp > 0:
            remainder = temp % 10
            reverse = (reverse * 10) + remainder
            temp = temp // 10
        if num == reverse:
            return True
        else:
            return False



p = Solution()
x =-242
print(p.isPalindrome(x))
