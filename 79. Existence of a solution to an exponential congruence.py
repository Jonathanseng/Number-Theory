def exists_solution_to_exponential_congruence(n, g, a, b):
  """
  Checks if there exists a solution to the exponential congruence ax ≡ b (mod n) with respect to the primitive root g.

  Args:
    n: The modulus.
    g: The primitive root.
    a: The base of the exponent.
    b: The modulus of the exponent.

  Returns:
    True if there exists a solution, False otherwise.
  """

  if not is_primitive_root(n, g):
    raise ValueError("g is not a primitive root of n")

  if not exists_mth_root(n, b - a, g):
    return False

  return True
