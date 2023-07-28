def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def prime_sieve(n):
  """Returns a list of the primes from 2 to n."""
  primes = []
  is_prime = [True] * (n + 1)
  for i in range(2, n + 1):
    if is_prime[i]:
      primes.append(i)
      for j in range(i * i, n + 1, i):
        is_prime[j] = False
  return primes

def main():
  n = 100
  primes = prime_sieve(n)
  print(primes)

if __name__ == "__main__":
  main()
