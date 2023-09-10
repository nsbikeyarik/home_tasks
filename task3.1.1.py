def count_list(data):
    result = str()
    for substring in data:
        result = result + substring[0]
    return result

data = ['asdfhgk', 'dfs', 'sfdghhgj']
count_list(data)
print(count_list(data))
