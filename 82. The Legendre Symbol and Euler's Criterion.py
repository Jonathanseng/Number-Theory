def legendre_symbol(n, p):
  """
  Calculates the Legendre symbol of n modulo p.

  Args:
    n: The number.
    p: The modulus.

  Returns:
    The Legendre symbol of n modulo p.
  """

  if n == 0:
    return 0

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  if n % p == 0:
    return p

  g = 2
  while g * g <= p:
    if pow(g, (p + 1) / 2, p) == n:
      return 1
    elif pow(g, (p + 1) / 2, p) == p - n:
      return -1
    g += 1

  return 0

def main():
  n = 3
  p = 5

  legendre_symbol_result = legendre_symbol(n, p)

  print("The Legendre symbol of n modulo p:")
  print(legendre_symbol_result)

if __name__ == "__main__":
  main()
