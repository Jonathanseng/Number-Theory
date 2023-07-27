def some_properties_of_integer_congruence():
  """Demonstrates some properties of integer congruence."""
  a = 10
  b = 12
  n = 15
  print("a congruent to b modulo n:", is_congruent_modulo(a, b, n)) # True
  print("a + n congruent to b + n modulo n:", is_congruent_modulo(a + n, b + n, n)) # True
  print("a * n congruent to b * n modulo n:", is_congruent_modulo(a * n, b * n, n)) # True
  print("a - n congruent to b - n modulo n:", is_congruent_modulo(a - n, b - n, n)) # True
  print("-a congruent to -b modulo n:", is_congruent_modulo(-a, -b, n)) # True

if __name__ == "__main__":
  some_properties_of_integer_congruence()
