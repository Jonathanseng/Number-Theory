def division_algorithm(dividend, divisor):
  """Returns the quotient and remainder of the division of dividend by divisor."""
  quotient = 0
  remainder = dividend
  while remainder >= divisor:
    quotient += 1
    remainder -= divisor
  return quotient, remainder

def main():
  dividend = 14
  divisor = 5
  quotient, remainder = division_algorithm(dividend, divisor)
  print("The quotient is", quotient)
  print("The remainder is", remainder)

if __name__ == "__main__":
  main()
