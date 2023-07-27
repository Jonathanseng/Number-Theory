def gcd(a, b):
  """Returns the greatest common divisor of a and b."""
  while b != 0:
    a, b = b, a % b
  return a

def main():
  a = 14
  b = 5
  print("The greatest common divisor of", a, "and", b, "is", gcd(a, b))

if __name__ == "__main__":
  main()
