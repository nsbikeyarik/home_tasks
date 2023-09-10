class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for x in range(0, n):
            for y in range(x + 1, n):
                if nums[x] + nums[y] == target:
                    return x, y
        return[]



p = Solution()
nums = [3,2,4]
target = 6
print(p.twoSum(nums, target))
