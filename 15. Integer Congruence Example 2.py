def integer_congruence_example_2():
  """Demonstrates the integer congruence a ≡ b (mod n) if and only if a + kn ≡ b (mod n) for any integer k."""
  a = 10
  b = 12
  n = 15
  k = 3
  print("a ≡ b (mod n):", is_congruent_modulo(a, b, n)) # True
  print("a + kn ≡ b (mod n):", is_congruent_modulo(a + k * n, b, n)) # True

if __name__ == "__main__":
  integer_congruence_example_2()
