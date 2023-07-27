def fundamental_theorem_of_arithmetic(n):
  """Returns the canonical representation of n."""
  primes = lemma1(n)
  representation = []
  for p in primes:
    power = 0
    while n % p == 0:
      power += 1
      n //= p
    representation.append((p, power))
  return representation

def main():
  n = 120
  representation = fundamental_theorem_of_arithmetic(n)
  print(representation)

if __name__ == "__main__":
  main()
