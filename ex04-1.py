# ex04-1.py

def sum_n(n):
  if n<1 :
    return 0
  return n+sum_n(n-1)

print(sum_n(100))


