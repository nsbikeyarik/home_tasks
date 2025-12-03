from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = m - 1
        y = n - 1
        k = m + n - 1
        while x >= 0 and y >= 0:
            if nums1[x] > nums2[y]:
                nums1[k] = nums1[x]
                x -= 1
            else:
                nums1[k] = nums2[y]
                y -= 1
            k -= 1
        while y >= 0:
            nums1[k] = nums2[y]
            y -= 1
            k -= 1




p=Solution()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(p.merge(nums1, m, nums2, n))