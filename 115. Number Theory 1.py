def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def prime_factorization(n):
  """Returns a list of the prime factors of n."""
  factors = []
  while n % 2 == 0:
    factors.append(2)
    n //= 2
  for i in range(3, int(n**0.5) + 1, 2):
    while n % i == 0:
      factors.append(i)
      n //= i
  return factors

def main():
  n = 15
  factors = prime_factorization(n)
  print(factors)

if __name__ == "__main__":
  main()
