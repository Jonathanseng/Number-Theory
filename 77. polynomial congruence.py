def solve_polynomial_congruence(n, f, g, x):
  """
  Solves the polynomial congruence f(x) ≡ g(x) (mod n).

  Args:
    n: The modulus.
    f: The polynomial of the left-hand side.
    g: The polynomial of the right-hand side.
    x: The unknown variable.

  Returns:
    The solution to the polynomial congruence f(x) ≡ g(x) (mod n).
  """

  if not is_primitive_root(n, 2):
    raise ValueError("2 is not a primitive root of n")

  if not exists_mth_root(n, f(0) - g(0), 2):
    raise ValueError("There does not exist an mth root of x - a modulo n")

  index = discrete_root(n, 2, f(0) - g(0))

  return pow(2, index, n)
