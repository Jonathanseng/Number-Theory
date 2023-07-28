def solve_exponential_congruence(n, g, a, b, x):
  """
  Solves the exponential congruence ax ≡ b (mod n) with respect to the primitive root g.

  Args:
    n: The modulus.
    g: The primitive root.
    a: The base of the exponent.
    b: The modulus of the exponent.
    x: The unknown variable.

  Returns:
    The solution to the exponential congruence ax ≡ b (mod n).
  """

  if not is_primitive_root(n, g):
    raise ValueError("g is not a primitive root of n")

  if not exists_mth_root(n, b - a, g):
    raise ValueError("There does not exist an mth root of x - a modulo n")

  index = discrete_root(n, g, b - a)

  return pow(g, index, n)
