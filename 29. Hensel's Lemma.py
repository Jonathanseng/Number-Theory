def hensels_lemma(f, p, a, n):
  """Returns the unique solution to f(x) ≡ 0 (mod p^n) in the interval (a, a + p^n)."""
  if n == 0:
    return a
  k = 0
  while not f(a + k * p ** (n - 1)) % p ** n == 0:
    k += 1
  x = a + k * p ** (n - 1)
  while x < a + p ** n:
    if f(x) % p ** n == 0:
      return x
    x += p ** (n - 1)
  raise ValueError("No solution")

def main():
  f = lambda x: x ** 2 + 1
  p = 3
  a = 2
  n = 2
  x = hensels_lemma(f, p, a, n)
  print(x)

if __name__ == "__main__":
  main()
