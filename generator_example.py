def custom_generator(n):
    for item in range(0, n):
        print(item)
        yield item

gen1 = custom_generator(5)

value = next(gen1)
next(gen1)
next(gen1)
next(gen1)
next(gen1)