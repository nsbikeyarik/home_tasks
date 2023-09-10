def sum_digits_string(str1):
  sum_digit = 0
  for x in str1:
    if x.isdigit():
      sum_digit = sum_digit + int(x)

  return sum_digit

print(sum_digits_string("b54b7k34bk23l5nb74j23jk436nl574547"))