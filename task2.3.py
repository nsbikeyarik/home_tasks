data = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
new_list = [item for sublist in data for item in sublist]
print(new_list)