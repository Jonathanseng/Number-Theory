def are_there_primitive_roots(n):
  """Returns True if there are primitive roots modulo n, False otherwise."""
  if n == 1:
    return False
  for i in range(2, n):
    if _is_primitive_root_helper(i, n):
      return True
  return False

def _is_primitive_root_helper(g, n):
  """Returns True if g is a primitive root modulo n, False otherwise."""
  if g == 1 or g == 0 or g % n == 1:
    return True
  for i in range(2, n):
    if pow(g, i, n) == 1:
      return False
  return True

if __name__ == "__main__":
  print(are_there_primitive_roots(10))
  print(are_there_primitive_roots(11))
