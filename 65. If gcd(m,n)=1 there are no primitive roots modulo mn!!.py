def there_are_no_primitive_roots_mod_mn_factorial(m, n):
  """
  Checks if there are no primitive roots modulo mn!!.

  Args:
    m: The first integer.
    n: The second integer.

  Returns:
    True if there are no primitive roots modulo mn!!, False otherwise.
  """

  # Check if m and n are positive integers.
  if m <= 0 or n <= 0:
    return False

  # Check if gcd(m,n) is equal to 1.
  if gcd(m, n) != 1:
    return False

  # Check if there are no primitive roots modulo mn!!.
  for i in range(2, mn + 1):
    if is_primitive_root(i, mn):
      return False

  return True

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
