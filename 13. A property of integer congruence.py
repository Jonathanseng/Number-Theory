def a_property_of_integer_congruence():
  """Demonstrates the property that if a is congruent to b modulo n, then ka is congruent to kb modulo n for any integer k."""
  a = 10
  b = 12
  n = 15
  k = 3
  print("a congruent to b modulo n:", is_congruent_modulo(a, b, n)) # True
  print("3a congruent to 3b modulo n:", is_congruent_modulo(3 * a, 3 * b, n)) # True

if __name__ == "__main__":
  a_property_of_integer_congruence()
