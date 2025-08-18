#sum of the factorial
def sum_fact(n):
  if n != 0:
    return n + sum_fact(n-1)
  return 0

sum_fact(5)
