def number_of_primitive_roots_mod_n(n):
  """
  Calculates the number of primitive roots modulo n.

  Args:
    n: The modulus.

  Returns:
    The number of primitive roots modulo n.
  """

  # Initialize the number of primitive roots.
  number_of_primitive_roots = 0

  # Iterate from 2 to n-1.
  for a in range(2, n):

    # If a is a primitive root modulo n, then increment the number of primitive roots.
    if is_primitive_root_mod_n(a, n):
      number_of_primitive_roots += 1

  # Return the number of primitive roots.
  return number_of_primitive_roots

if __name__ == "__main__":
  n = 17
  print("The number of primitive roots modulo {} is {}".format(n, number_of_primitive_roots_mod_n(n)))
