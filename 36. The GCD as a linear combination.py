def gcd_as_linear_combination(a, b):
  """Returns a linear combination of a and b that is equal to their GCD."""
  if a < b:
    temp = a
    a = b
    b = temp

  while b != 0:
    q = a // b
    r = a - q * b
    a = b
    b = r
  return a

def main():
  a = 15
  b = 12
  gcd = gcd_as_linear_combination(a, b)
  print(gcd)

if __name__ == "__main__":
  main()
