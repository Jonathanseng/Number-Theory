def inverse_modulo(a, m):
  """Returns the modular inverse of a modulo m, or None if no inverse exists."""
  gcd, u, v = _extended_euclidean_algorithm(a, m)
  if gcd != 1:
    return None
  else:
    return u % m

def _extended_euclidean_algorithm(a, b):
  """Returns the tuple (u, v) such that au + bv = gcd(a, b)."""
  if b == 0:
    return (1, 0)
  else:
    u, v = _extended_euclidean_algorithm(b, a % b)
    return (v, u - (a // b) * v)

def main():
  a = 3
  m = 11
  inverse = inverse_modulo(a, m)
  print(inverse)

if __name__ == "__main__":
  main()
