# recursion 1 to n even
def recursion(n):
  if n == 0:
    return
  recursion(n-1)
  if n%2 == 0:
    print("even:",n)
  else:
    print("odd:",n)

n = int(input())
result = recursion(n)
