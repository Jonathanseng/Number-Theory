def polynomial_congruence_proposition(f, m, a, b):
  """Returns True if f(x) ≡ 0 (mod m) for all x ∈ [a, b], False otherwise."""
  if a > b:
    raise ValueError("a must be less than or equal to b")
  for x in range(a, b + 1):
    if f(x) % m != 0:
      return False
  return True

def main():
  f = lambda x: x ** 2 + 1
  m = 3
  a = 2
  b = 5
  is_congruent = polynomial_congruence_proposition(f, m, a, b)
  print(is_congruent)

if __name__ == "__main__":
  main()
