def fermat_little_theorem(p, a):
  """Returns True if a^(p-1) ≡ 1 (mod p), False otherwise."""
  if not p > 1:
    raise ValueError("p must be greater than 1")
  return pow(a, p - 1, p) == 1

def main():
  p = 5
  a = 2
  is_congruent = fermat_little_theorem(p, a)
  print(is_congruent)

if __name__ == "__main__":
  main()
