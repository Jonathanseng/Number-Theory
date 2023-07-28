def chinese_remainder_theorem_proof(m, a):
  """Returns an integer x such that x % m[i] = a[i] for all i."""
  M = 1
  x = 0
  for mi, ai in zip(m, a):
    Mi = M // mi
    x = (x + Mi * ai) % M
  return x

def chinese_remainder_theorem_proof_helper(m, a):
  """Returns a proof of the Chinese Remainder Theorem."""
  for i in range(len(m)):
    if m[i] == 1:
      return True
  for i in range(len(m)):
    for j in range(i + 1, len(m)):
      if m[i] * m[j] % M != 1:
        return False
  return True

if __name__ == "__main__":
  m = [2, 3, 5]
  a = [1, 2, 3]
  x = chinese_remainder_theorem_proof(m, a)
  print(x)
  print(chinese_remainder_theorem_proof_helper(m, a))
