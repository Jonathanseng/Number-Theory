def is_prime(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def phi(n):
  """Returns the Euler's totient function of n."""
  phi = 1
  for i in range(2, n + 1):
    if is_prime(i):
      if n % i == 0:
        phi *= i - 1
      else:
        phi *= i
  return phi

def main():
  n = 15
  phi_n = phi(n)
  print(phi_n)

if __name__ == "__main__":
  main()
