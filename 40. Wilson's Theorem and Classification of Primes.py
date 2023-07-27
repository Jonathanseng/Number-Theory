def wilson_theorem(p):
  """Returns True if (p-1)! ≡ -1 (mod p), False otherwise."""
  if not p > 1:
    raise ValueError("p must be greater than 1")
  product = 1
  for i in range(1, p):
    product *= i
  return product % p == -1

def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def main():
  p = 5
  is_prime_wilson = wilson_theorem(p)
  is_prime_regular = is_prime(p)
  print(is_prime_wilson)
  print(is_prime_regular)

if __name__ == "__main__":
  main()
