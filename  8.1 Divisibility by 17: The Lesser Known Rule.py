def is_divisible_by_17(n):
  """Returns True if n is divisible by 17, False otherwise."""
  if n <= 17:
    return n in (0, 17)
  sum_of_digits = 0
  while n > 0:
    sum_of_digits += n % 10
    n //= 10
  if sum_of_digits % 17 == 0:
    return True
  else:
    return False

def main():
  n = 15
  is_divisible_by_17_n = is_divisible_by_17(n)
  print(is_divisible_by_17_n)

if __name__ == "__main__":
  main()
