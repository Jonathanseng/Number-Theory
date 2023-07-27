def is_congruent_modulo(a, b, n):
  """Returns True if a is congruent to b modulo n, False otherwise."""
  return a % n == b % n

def main():
  a = 10
  b = 12
  n = 15
  print(is_congruent_modulo(a, b, n)) # True
  print(is_congruent_modulo(a, 15, n)) # False

if __name__ == "__main__":
  main()
