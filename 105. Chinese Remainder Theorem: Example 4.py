def chinese_remainder_theorem_example4(m, a):
  """Returns an integer x such that x % m[i] = a[i] for all i."""
  M = 1
  x = 0
  for mi, ai in zip(m, a):
    Mi = M // mi
    x = (x + Mi * ai) % M
  return x

if __name__ == "__main__":
  m = [3, 5, 7]
  a = [2, 3, 2]
  x = chinese_remainder_theorem_example4(m, a)
  print(x)
