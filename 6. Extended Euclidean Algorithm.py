def extended_gcd(a, b):
  """Returns the greatest common divisor of a and b, and also the coefficients x and y such that
  ax + by = gcd(a, b)."""
  if a == 0:
    return b, 0, 1
  else:
    gcd, x, y = extended_gcd(b % a, a)
    return gcd, y - (b // a) * x, x

def main():
  a = 14
  b = 5
  gcd, x, y = extended_gcd(a, b)
  print("The greatest common divisor of", a, "and", b, "is", gcd)
  print("The coefficients x and y are", x, "and", y)

if __name__ == "__main__":
  main()
