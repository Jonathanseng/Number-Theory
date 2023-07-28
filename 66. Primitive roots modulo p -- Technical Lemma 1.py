def technical_lemma_1(p):
  """
  Checks if there are primitive roots modulo p.

  Args:
    p: The modulus.

  Returns:
    True if there are primitive roots modulo p, False otherwise.
  """

  # Check if p is an odd prime number.
  if p % 2 == 0 or not is_prime(p):
    return False

  # Check if there are primitive roots modulo p.
  for i in range(2, p):
    if is_primitive_root(i, p):
      return True

  return False

def is_primitive_root(a, p):
  """
  Checks if the integer a is a primitive root modulo p.

  Args:
    a: The integer.
    p: The modulus.

  Returns:
    True if the integer a is a primitive root modulo p, False otherwise.
  """

  # Check if a is an integer greater than 1 and less than p.
  if a <= 1 or a >= p:
    return False

  # Check if the order of a modulo p is p - 1.
  order_of_a = order_of_integer(a, p)
  if order_of_a != p - 1:
    return False

  # Check if a is a primitive root modulo p.
  for i in range(2, p):
    if pow(a, i) % p == 1:
      return False

  return True

def order_of_integer(a, p):
  """
  Calculates the order of the integer a mod p.

  Args:
    a: The integer.
    p: The modulus.

  Returns:
    The order of the integer a mod p.
  """

  # Initialize the order to 0.
  order = 0

  # Iterate over all positive integers.
  for i in range(1, p):

    # If a^(i * d) is congruent to 1 mod p, then the order of a mod p is i * d.
    if pow(a, i * order) % p == 1:
      return i * order

  return order

def is_prime(n):
  """
  Checks if the integer n is a prime number.

  Args:
    n: The integer.

  Returns:
    True if the integer n is a prime number, False otherwise.
  """

  # Check if n is a positive integer.
  if n <= 0:
    return False

  # Check if n is a prime number by checking if it is divisible by any integer from 2 to n - 1.
  for i in range(2, n):
    if n % i == 0:
      return False

  return True
