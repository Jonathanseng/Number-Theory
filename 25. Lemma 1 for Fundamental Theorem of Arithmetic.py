def lemma_1(n):
  """Returns the prime factorization of n."""
  primes = []
  while n % 2 == 0:
    primes.append(2)
    n //= 2
  for i in range(3, int(n ** 0.5) + 1, 2):
    while n % i == 0:
      primes.append(i)
      n //= i
  if n > 2:
    primes.append(n)
  return primes

def main():
  n = 120
  primes = lemma_1(n)
  print(primes)

if __name__ == "__main__":
  main()
