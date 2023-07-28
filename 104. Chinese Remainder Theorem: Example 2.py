def chinese_remainder_theorem_example2(m, a):
  """Returns an integer x such that x % m[i] = a[i] for all i."""
  M = m[0]
  x = a[0]
  for mi, ai in zip(m[1:], a[1:]):
    M *= mi
    x = (x + (M // mi) * ai) % M
  return x

if __name__ == "__main__":
  m = [2, 3, 5]
  a = [1, 2, 3]
  x = chinese_remainder_theorem_example2(m, a)
  print(x)
