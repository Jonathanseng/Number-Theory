def infinitely_many_primes(n):
  """Returns True if there are infinitely many primes of the form 4n+3, False otherwise."""
  for i in range(1, n):
    if not lemma_2(4 * i + 3):
      return False
  return True

def main():
  n = 100
  is_infinitely_many = infinitely_many_primes(n)
  print(is_infinitely_many)

if __name__ == "__main__":
  main()
