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

def euler_theorem(a, n):
  """
  Checks if Euler's Theorem holds for a given number a and n.

  Args:
    a: The number to test.
    n: The modulus.

  Returns:
    True if Euler's Theorem holds, False otherwise.
  """
  return (a ** (phi(n) - 1)) % n == 1

def main():
  a = 10
  n = 17
  print("Does Euler's Theorem hold for a={} and n={}? {}".format(a, n, euler_theorem(a, n)))

if __name__ == "__main__":
  main()
