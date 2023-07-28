def is_primitive_root(n, g):
  """
  Returns True if g is a primitive root of n, False otherwise.

  Args:
    n: The number to find the primitive root of.
    g: The potential primitive root.

  Returns:
    True if g is a primitive root of n, False otherwise.
  """

  if g == 1 or g == n - 1:
    return False

  for i in range(2, n):
    if gcd(i, n) != 1:
      continue

    if pow(g, i, n) == 1:
      return False

  return True

def find_primitive_roots(n):
  """
  Finds all the primitive roots of n.

  Args:
    n: The number to find the primitive roots of.

  Returns:
    A list of all the primitive roots of n.
  """

  primitive_roots = []

  for g in range(2, n):
    if is_primitive_root(n, g):
      primitive_roots.append(g)

  return primitive_roots

if __name__ == "__main__":
  print(find_primitive_roots(54))
