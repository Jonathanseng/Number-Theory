def chinese_remainder(congruences):
  """Returns the smallest positive integer x such that x ≡ r[i] (mod m[i]) for all i."""
  product = 1
  for m, r in congruences:
    product *= m
  remainders = [r * product // m for m, r in congruences]
  x = 0
  for r in remainders:
    x += r
  x %= product
  return x

def main():
  congruences = [(7, 10), (12, 11), (13, 2)]
  x = chinese_remainder(congruences)
  print(x)

if __name__ == "__main__":
  main()
