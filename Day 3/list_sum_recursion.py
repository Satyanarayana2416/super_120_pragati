# sum of list using recursion
def sum_list(n):
  list_a = []
  if n != 0:
    sum_list(n-1)
    list_a+=[n]
  print(list_a)
sum_list(5)
