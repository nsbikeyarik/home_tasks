#iterator
data = [1, 2, 3, 4, 5]
new_data = iter(data)
value = next(new_data)
value = next(new_data)
value = next(new_data)
# print(value)

#generator
def generator(n):
    for item in range(0, n):
        print(item)
        yield item

generator1= generator(5)
value =next(generator1)
value =next(generator1)
value =next(generator1)
value =next(generator1)

