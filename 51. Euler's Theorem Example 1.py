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

def euler_theorem_example_1():
  a = 12
  n = 17
  print("Does Euler's Theorem hold for a={} and n={}? {}".format(a, n, (a ** (phi(n) - 1)) % n == 1))

if __name__ == "__main__":
  euler_theorem_example_1()
