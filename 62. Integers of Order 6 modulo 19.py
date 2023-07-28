def integers_of_order_6_mod_19():
  """
  Finds all integers of order 6 mod 19.

  Returns:
    A list of integers of order 6 mod 19.
  """

  # Create a list to store the integers of order 6 mod 19.
  integers_of_order_6 = []

  # Iterate over all integers from 0 to 19.
  for i in range(19):

    # If the integer is of order 6 mod 19, add it to the list.
    if order_of_integer(i, 6, 19) == 6:
      integers_of_order_6.append(i)

  return integers_of_order_6

def order_of_integer(a, d, p):
  """
  Calculates the order of the integer a mod p.

  Args:
    a: The integer.
    d: The order.
    p: The modulus.

  Returns:
    The order of the integer a mod p.
  """

  # Initialize the order to 0.
  order = 0

  # Iterate over all positive integers.
  for i in range(1, p):

    # If a^(i * d) is congruent to 1 mod p, then the order of a mod p is i * d.
    if pow(a, i * d) % p == 1:
      order = i * d
      break

  return order
