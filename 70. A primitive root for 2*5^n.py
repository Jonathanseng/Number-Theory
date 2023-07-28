def primitive_root_for_2_5_n(n):
  """
  Finds a primitive root modulo 2 * 5^n.

  Args:
    n: The exponent.

  Returns:
    A primitive root modulo 2 * 5^n.
  """

  # Check if n is a positive integer.
  if n <= 0:
    return None

  # Find a primitive root modulo 5^n.
  primitive_root_mod_5_n = technical_lemma_2(5**n)

  # Check if the primitive root modulo 5^n is also a primitive root modulo 2 * 5^n.
  if is_primitive_root(primitive_root_mod_5_n, 2 * 5**n):
    return primitive_root_mod_5_n
  else:
    return None

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

def technical_lemma_2(p):
  """
  Finds all primitive roots modulo p.

  Args:
    p: The modulus.

  Returns:
    A list of all primitive roots modulo p.
  """


  # Check if p is an odd prime number.
  if p % 2 == 0 or not is_prime(p):
    return []

  # Find all primitive roots modulo p.
  primitive_roots_mod_p = []
  for i in range(2, p):
    if is_primitive_root_2(i, p):
      primitive_roots_mod_p.append(i)

  return primitive_roots_mod_p

def is_primitive_root_2(a, p):
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

  # Check if the order of a modulo p is (p - 1) / 2.
  order_of_a = order_of_integer_2(a, p)
  if order_of_a != (p - 1) / 2:
    return False

  # Check if a is a primitive root modulo p.
  for i in range(2, p):
    if pow(a, i) % p == 1:
      return False

  return True

def
