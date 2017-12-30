# ex05-1.py
def pibo(n):
  if n<=1 :
    return n;

  return pibo(n-2) + pibo(n-1)

print(pibo(7))
