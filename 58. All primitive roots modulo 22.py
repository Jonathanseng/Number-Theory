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

def all_primitive_roots_mod_n(n):
  """
  Calculates all primitive roots modulo n.

  Args:
    n: The modulus.

  Returns:
    A list of all primitive roots modulo n.
  """

  # Initialize the list of primitive roots.
  primitive_roots = []

  # Iterate from 2 to n-1.
  for a in range(2, n):

    # If a is a primitive root modulo n, then add it to the list.
    if is_primitive_root_mod_n(a, n):
      primitive_roots.append(a)

  # Return the list of primitive roots.
  return primitive_roots

if __name__ == "__main__":
  n = 22
  primitive_roots = all_primitive_roots_mod_n(n)
  print("The primitive roots modulo {} are {}".format(n, primitive_roots))
