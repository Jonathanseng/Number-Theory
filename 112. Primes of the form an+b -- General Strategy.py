def primes_of_the_form_an_b(a, b, n):
  """Returns a list of all primes of the form an+b from 1 to n."""
  primes = []
  for i in range(1, n + 1):
    if is_prime(i + b):
      primes.append(i + b)
  return primes

def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

if __name__ == "__main__":
  for prime in primes_of_the_form_an_b(2, 1, 100):
    print(prime)
