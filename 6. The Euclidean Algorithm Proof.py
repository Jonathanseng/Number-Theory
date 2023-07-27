def gcd(a, b):
  """Returns the greatest common divisor of a and b."""
  while b != 0:
    t = a % b
    a = b
    b = t
  return a

def main():
  a = 14
  b = 5
  print("The greatest common divisor of", a, "and", b, "is", gcd(a, b))

if __name__ == "__main__":
  main()
