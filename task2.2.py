def count_lists(data):
    result = list()
    for sublist in data:
       result = result + sublist

    return result

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(count_lists(data))