my_list = [1, 2, 3, 4, 5, -8, 2, 6, 7, 8, 9]
iter_object = iter(my_list)
while True:
    try:
        my_list1 = next(iter_object)
        if my_list1 >= 0:
            print(my_list1)
        else:
            break
    except StopIteration:
        break





