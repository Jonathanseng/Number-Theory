def there_is_a_primitive_root_mod_2p_n_factorial(p, n):
  """
  Checks if there is a primitive root modulo 2p^n.

  Args:
    p: The first integer.
    n: The second integer.

  Returns:
    True if there is a primitive root modulo 2p^n, False otherwise.
  """

  # Check if p is a positive integer.
  if p <= 0:
    return False

  # Check if n is a positive integer.
  if n <= 0:
    return False

  # Check if there is a primitive root modulo 2p^n.
  for i in range(2, 2 * p ** n + 1):
    if is_primitive_root(i, 2 * p ** n):
      return True

  return False

def is_primitive_root(a, n):
  """
  Checks if the integer a is a primitive root modulo n.

  Args:
    a: The integer.
    n: The modulus.

  Returns:
    True if the integer a is a primitive root modulo n, False otherwise.
  """

  # Check if a is an integer greater than 1 and less than n.
  if a <= 1 or a >= n:
    return False

  # Check if the order of a modulo n is n - 1.
  order_of_a = order_of_integer(a, n)
  if order_of_a != n - 1:
    return False

  # Check if a is a primitive root modulo n.
  for i in range(2, n):
    if pow(a, i) % n == 1:
      return False

  return True

def order_of_integer(a, n):
  """
  Calculates the order of the integer a mod n.

  Args:
    a: The integer.
    n: The modulus.

  Returns:
    The order of the integer a mod n.
  """

  # Initialize the order to 0.
  order = 0

  # Iterate over all positive integers.
  for i in range(1, n):

    # If a^(i * d) is congruent to 1 mod n, then the order of a mod n is i * d.
    if pow(a, i * order) % n == 1:
      return i * order

  return order
