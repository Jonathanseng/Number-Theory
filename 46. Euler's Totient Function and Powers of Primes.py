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

def powers_of_primes(n):
  """
  Calculates the powers of primes up to a given number n.

  Args:
    n: The number to calculate the powers of primes for.

  Returns:
    A list of the powers of primes up to n.
  """
  powers = []
  for i in range(2, n + 1):
    power = 1
    while i % 2 == 0:
      power *= 2
      i //= 2
    for p in range(3, int(math.sqrt(i)) + 1, 2):
      while i % p == 0:
        power *= p
        i //= p
    if i > 1:
      power *= i
    powers.append(power)
  return powers

if __name__ == "__main__":
  n = 100
  phi_n = phi(n)
  powers = powers_of_primes(n)
  print("Euler's Totient Function of {} is {}".format(n, phi_n))
  print("The powers of primes up to {} are {}".format(n, powers))
