def my_condition(v):
  return v % 2 == 0

def do_if_pass(l):
  list_okay = True
  for v in l:
    if not my_condition(v):
      list_okay = False

  if list_okay:
    print( 'everything in list is okay, including'),
    for v in l:
      print (v),
    print
  else:
    print ('not okay')

do_if_pass([1,2,3])
do_if_pass([2,4,6])