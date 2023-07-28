import math
import numpy as np

def phi(n):
  """
  Calculates Euler's Totient Function for a given number n.

  Args:
    n: The number to calculate the Totient Function for.

  Returns:
    The Totient Function of n.
  """
  phi = n
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      phi -= phi / i
      while n % i == 0:
        n //= i
  if n > 1:
    phi -= phi / n
  return phi

def phi_product(m, n):
  """
  Calculates the product of Euler's Totient Functions of m and n.

  Args:
    m: The first number to calculate the Totient Function for.
    n: The second number to calculate the Totient Function for.

  Returns:
    The product of the Totient Functions of m and n.
  """
  return phi(m) * phi(n)

def is_multiplicative(n):
  """
  Checks if Euler's Totient Function is multiplicative for a given number n.

  Args:
    n: The number to check.

  Returns:
    True if Euler's Totient Function is multiplicative for n, False otherwise.
  """
  for i in range(2, n):
    if phi_product(i, n) != phi(n * i):
      return False
  return True

if __name__ == "__main__":
  n = 100
  print("Is Euler's Totient Function multiplicative for 100? {}".format(is_multiplicative(n)))
