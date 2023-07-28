def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def find_next_prime(n):
  """Returns the next prime number after n."""
  while True:
    n += 1
    if is_prime(n):
      return n
