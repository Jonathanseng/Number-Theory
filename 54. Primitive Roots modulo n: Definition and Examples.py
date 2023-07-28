def is_primitive_root_mod_n(a, n):
  """
  Checks if a is a primitive root modulo n.

  Args:
    a: The number to check.
    n: The modulus.

  Returns:
    True if a is a primitive root modulo n, False otherwise.
  """

  # Check if a is coprime to n.
  if math.gcd(a, n) != 1:
    return False

  # Iterate from 1 to n - 1.
  for i in range(1, n):

    # If a ** i is 1 modulo n, then a is not a primitive root modulo n.
    if (a ** i) % n == 1:
      return False

  # a is a primitive root modulo n.
  return True

if __name__ == "__main__":
  n = 17
  for i in range(2, n + 1):
    if is_primitive_root_mod_n(i, n):
      print("{} is a primitive root modulo {}".format(i, n))
