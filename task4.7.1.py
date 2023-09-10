data = '1234567890abcdefg'
a = 0
b = 3
while True:
    print(data[a:b])
    a = a + 3
    b = b + 3
    if b > len(data) -1:
        break


