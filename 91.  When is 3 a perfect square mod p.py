def is_3_a_perfect_square_mod_p(p):
  """Returns True if 3 is a perfect square mod p, False otherwise."""
  for i in range(2, p):
    if (i * i) % p == 3:
      return True
  return False

if __name__ == "__main__":
  for p in range(2, 100):
    print(p, is_3_a_perfect_square_mod_p(p))
