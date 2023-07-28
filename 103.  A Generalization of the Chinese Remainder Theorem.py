def chinese_remainder_theorem_generalized(m, a):
  """Returns an integer x such that x % m[i] = a[i] for all i."""
  M = 1
  for mi in m:
    M *= mi
  x = 0
  for mi, ai in zip(m, a):
    x += (M // mi) * ai
  return x % M

if __name__ == "__main__":
  m = [2, 3, 5]
  a = [1, 2, 3]
  x = chinese_remainder_theorem_generalized(m, a)
  print(x)
