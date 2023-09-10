def count_list(data):
    result = str()
    for substring in data:
        if len(substring) >=4:
            print("result bigger than 4")
        else:
            print("result smaller than 4")

data = ['asdfhgk', 'dfs', 'sfdghhgj']
count_list(data)
