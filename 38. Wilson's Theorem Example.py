def wilson_theorem(p):
  """Returns True if (p-1)! ≡ -1 (mod p), False otherwise."""
  if not p > 1:
    raise ValueError("p must be greater than 1")
  product = 1
  for i in range(1, p):
    product *= i
  return product % p == -1

def main():
  p = 5
  is_congruent = wilson_theorem(p)
  print(is_congruent)

if __name__ == "__main__":
  main()
