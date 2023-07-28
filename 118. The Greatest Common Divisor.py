def gcd(a, b):
  """Returns the greatest common divisor of a and b."""
  if a < b:
    a, b = b, a
  while b != 0:
    temp = a % b
    a = b
    b = temp
  return a

def main():
  a = 15
  b = 10
  gcd_ab = gcd(a, b)
  print(gcd_ab)

if __name__ == "__main__":
  main()
