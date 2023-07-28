def chinese_remainder_theorem_example3(m, a):
  """Returns an integer x such that x % m[i] = a[i] for all i."""
  M = m[0] * m[1]
  x = a[0] * m[1] + a[1] * m[0]
  for mi, ai in zip(m[2:], a[2:]):
    Mi = M // mi
    x = (x + Mi * ai) % M
  return x

if __name__ == "__main__":
  m = [2, 3, 5]
  a = [1, 2, 3]
  x = chinese_remainder_theorem_example3(m, a)
  print(x)
