def discrete_root(n, g, x):
  """
  Returns the discrete root of x with respect to the primitive root g modulo n.

  Args:
    n: The modulus.
    g: The primitive root.
    x: The number to find the discrete root of.

  Returns:
    The discrete root of x with respect to the primitive root g modulo n.
  """

  if not is_primitive_root(n, g):
    raise ValueError("g is not a primitive root of n")

  if x == 0:
    return 0

  index = index_with_respect_to_primitive_root(n, g, x)

  return pow(g, index, n)
