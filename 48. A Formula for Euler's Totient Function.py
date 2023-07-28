import math

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

def phi_formula(n):
  """
  Calculates Euler's Totient Function for a given number n using the formula.

  Args:
    n: The number to calculate the Totient Function for.

  Returns:
    The Totient Function of n.
  """
  phi = n
  for i in range(2, n):
    if math.gcd(n, i) == 1:
      phi -= phi / i
  return phi

if __name__ == "__main__":
  n = 100
  phi_n = phi(n)
  phi_n_formula = phi_formula(n)
  print("Euler's Totient Function of {} is {}".format(n, phi_n))
  print("Euler's Totient Function of {} using the formula is {}".format(n, phi_n_formula))
