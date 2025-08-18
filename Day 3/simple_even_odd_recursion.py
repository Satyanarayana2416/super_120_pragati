# recursion 1 to n even
def recursion(n):
  if n == 0:
    return
  recursion(n-1)
  print(f"{n} is Even" if n%2 == 0 else f"{n} is odd")

n = int(input())
result = recursion(n)
