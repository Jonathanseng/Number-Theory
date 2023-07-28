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

  indices = []
  for i in range(1, n):
    if pow(g, i, n) == x:
      indices.append(i)

  if len(indices) == 0:
    raise ValueError("x has no discrete root with respect to g modulo n")

  return indices[0]
