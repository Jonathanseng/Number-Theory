def fermat_little_theorem(p, a):
  """Returns True if a^(p-1) ≡ 1 (mod p), False otherwise."""
  if not p > 1:
    raise ValueError("p must be greater than 1")
  return pow(a, p - 1, p) == 1

def corollary_1(p, a):
  """Returns True if ap ≡ a (mod p), False otherwise."""
  return fermat_little_theorem(p, a) - 1 == 0

def corollary_2(p, a):
  """Returns True if a^(p-2) ≡ 1 (mod p), False otherwise."""
  return pow(a, p - 2, p) == 1

def main():
  p = 5
  a = 2
  is_congruent_1 = corollary_1(p, a)
  is_congruent_2 = corollary_2(p, a)
  print(is_congruent_1)
  print(is_congruent_2)

if __name__ == "__main__":
  main()
