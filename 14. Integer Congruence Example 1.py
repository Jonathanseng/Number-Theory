def integer_congruence_example_1():
  """Demonstrates the integer congruence a ≡ b (mod n) if and only if a - b is divisible by n."""
  a = 10
  b = 12
  n = 15
  print("a ≡ b (mod n):", is_congruent_modulo(a, b, n)) # True
  print("a - b is divisible by n:", (a - b) % n == 0) # True

if __name__ == "__main__":
  integer_congruence_example_1()
