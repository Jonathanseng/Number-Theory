def generate_primitive_pythagorean_triples(limit):
  """Generates all primitive Pythagorean triples less than or equal to limit."""
  for m in range(2, limit + 1):
    for n in range(1, int(m ** 0.5) + 1):
      if m % n == 0:
        continue
      else:
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        if gcd(a, b) == 1:
          yield a, b, c

def main():
  for a, b, c in generate_primitive_pythagorean_triples(1000):
    print(a, b, c)

if __name__ == "__main__":
  main()
