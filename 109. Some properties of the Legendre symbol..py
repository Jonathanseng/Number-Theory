def legendre_symbol(a, p):
  """Returns the Legendre symbol of a and p."""
  if a % p == 0:
    return 0
  if p == 2:
    return 1 if a % 2 == 1 else -1
  if a < 0:
    a = -a
  s = 1
  for i in range(1, p):
    s *= (-1 if i % 2 == 1 else 1)
    if a == i:
      return s
    elif a % i == 0:
      return 0
  return s

def properties_of_legendre_symbol():
  """Returns some properties of the Legendre symbol."""
  print("The Legendre symbol of 2 and 3 is", legendre_symbol(2, 3))
  print("The Legendre symbol of 3 and 5 is", legendre_symbol(3, 5))
  print("The Legendre symbol of 1 and 2 is", legendre_symbol(1, 2))
  print("The Legendre symbol of -1 and 2 is", legendre_symbol(-1, 2))

if __name__ == "__main__":
  properties_of_legendre_symbol()
