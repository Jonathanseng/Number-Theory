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

def find_largest_prime_factor(n):
  """Returns the largest prime factor of n."""
  while n % 2 == 0:
    n //= 2
  for i in range(3, int(n**0.5) + 1, 2):
    while n % i == 0:
      n //= i
  return n

def main():
  n = 600851475143
  largest_prime_factor = find_largest_prime_factor(n)
  print(largest_prime_factor)

if __name__ == "__main__":
  main()
