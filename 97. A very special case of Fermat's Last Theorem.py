def fermat_special_case(n):
  """Returns True if n^3 + n^2 + 1 is a prime number, False otherwise."""
  if n < 2:
    return False
  for i in range(2, n):
    if (n ** 3) + (n ** 2) + 1 == i ** 2:
      return False
  return True

if __name__ == "__main__":
  for n in range(2, 10):
    print(n, fermat_special_case(n))
