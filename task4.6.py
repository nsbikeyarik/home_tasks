numbers = [(23, 'data', 56), (None, 1034, 54), (254, [1, 2] , 5), (45, 2), (122, 63, 74)]
iter_object = iter(numbers)

while True:
    try:
        my_list1 = next(iter_object)
        only_int = True
        for x in my_list1:
            if not isinstance(x, int):
                only_int = False
                break

        if not only_int:
            continue

        print(my_list1)
        break
    except StopIteration:
        break



