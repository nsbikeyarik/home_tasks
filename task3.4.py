def count_list2(a1, b1):
    new_list = []
    for element in a1:
        if element in b1 and element not in new_list:
            new_list.append(element)


    return new_list

a1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(count_list2(a1, b1))