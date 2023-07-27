def is_divisible_by_2(number):
  """Returns True if the number is divisible by 2, False otherwise."""
  return number % 2 == 0

def is_divisible_by_3(number):
  """Returns True if the number is divisible by 3, False otherwise."""
  sum_of_digits = 0
  for digit in str(number):
    sum_of_digits += int(digit)
  return sum_of_digits % 3 == 0

def is_divisible_by_5(number):
  """Returns True if the number is divisible by 5, False otherwise."""
  return number % 5 == 0

def is_divisible_by_7(number):
  """Returns True if the number is divisible by 7, False otherwise."""
  sum_of_digits = 0
  for digit in str(number):
    sum_of_digits += int(digit)
  if sum_of_digits % 7 == 0:
    return True
  else:
    return False

def main():
  number = 14
  print(is_divisible_by_2(number))
  print(is_divisible_by_3(number))
  print(is_divisible_by_5(number))
  print(is_divisible_by_7(number))

if __name__ == "__main__":
  main()
