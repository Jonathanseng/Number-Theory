def exists_mth_root(n, m, g):
  """
  Returns True if there exists an mth root of n with respect to the primitive root g modulo n, False otherwise.

  Args:
    n: The modulus.
    m: The desired power.
    g: The primitive root.

  Returns:
    True if there exists an mth root of n with respect to the primitive root g modulo n, False otherwise.
  """

  if not is_primitive_root(n, g):
    raise ValueError("g is not a primitive root of n")

  if m == 0:
    return True

  for i in range(1, n):
    if pow(g, i * m, n) == 1:
      return True

  return False
