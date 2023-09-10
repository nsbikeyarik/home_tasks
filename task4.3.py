def check_number(func):
   def wrapper(a, b):
      if a > 2 and b < 6 :
         print("Good")
         return func(a, b)
      else:
         print("That bad")

   return wrapper


@check_number
def average(a, b):
   return (a + b)/2

result = average(3, 4)
print(result)

