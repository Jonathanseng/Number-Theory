def is_quadratic_residue(n, p):
  """
  Checks if n is a quadratic residue modulo p.

  Args:
    n: The number to check.
    p: The modulus.

  Returns:
    True if n is a quadratic residue modulo p, False otherwise.
  """

  if n == 0:
    return True

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  if n % p == 0:
    return True

  g = 2
  while g * g <= p:
    if pow(g, (p + 1) / 2, p) == n:
      return True
    g += 1

  return False

def main():
  n = 3
  p = 5

  is_quadratic_residue_result = is_quadratic_residue(n, p)

  print("Is n a quadratic residue modulo p:")
  print(is_quadratic_residue_result)

if __name__ == "__main__":
  main()
