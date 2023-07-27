def lemma_2(n):
  """Returns True if n is prime, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

def main():
  n = 120
  is_prime = lemma_2(n)
  print(is_prime)

if __name__ == "__main__":
  main()
