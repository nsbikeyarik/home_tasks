class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list1= list1 + list2
        a = len(list1)
        for x in range(0, a):
            for y in range(x + 1, a):
                 if list1[y] < list1[x]:
                    temp = list1[y]
                    list1[y] = list1[x]
                    list1[x] = temp
        print(list1)

p =  Solution()
list1 = [35, 0, 31, 11, 26]
list2 = [3, 2, 5, 7, 12, 35]
p.mergeTwoLists(list1, list2)