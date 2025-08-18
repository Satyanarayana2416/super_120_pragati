def sum_list(i,num,n):
  if i == n:
    return 0
  return num[i] + sum_list(i+1,num,n)
n = [1,2,3,4,5]
sum_list(0,n,len(n))
