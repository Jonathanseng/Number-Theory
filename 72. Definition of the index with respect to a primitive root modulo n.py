def index_with_respect_to_primitive_root(n, g, x):
  """
  Returns the index of x with respect to the primitive root g modulo n.

  Args:
    n: The modulus.
    g: The primitive root.
    x: The number to find the index of.

  Returns:
    The index of x with respect to the primitive root g modulo n.
  """

  if not is_primitive_root(n, g):
    raise ValueError("g is not a primitive root of n")

  if x == 0:
    return 0

  index = 1
  while pow(g, index, n) != x:
    index += 1

  return index
