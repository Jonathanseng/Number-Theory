def linear_diophantine(a, b, c):
  """Returns a tuple of two numbers x and y such that ax + by = c, or None if no such solution exists."""
  gcd, x, y = extended_gcd(a, b)
  if c % gcd != 0:
    return None
  else:
    return x * (c // gcd), y * (c // gcd)

def main():
  a = 14
  b = 5
  c = 12
  x, y = linear_diophantine(a, b, c)
  if x is None:
    print("No solution exists.")
  else:
    print("x = ", x, "and y = ", y)

if __name__ == "__main__":
  main()
