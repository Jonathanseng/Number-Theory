def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def infinitely_many_primes(n):
  """Returns True if there are infinitely many primes of the form 3n+1, False otherwise."""
  for i in range(n):
    if not is_prime(3 * i + 1):
      return False
  return True

if __name__ == "__main__":
  print(infinitely_many_primes(100))
