def integers_of_order_d_mod_p(d, p):
  """
  Finds all integers of order d mod p.

  Args:
    d: The order.
    p: The modulus.

  Returns:
    A list of integers of order d mod p.
  """

  # Create a list to store the integers of order d mod p.
  integers_of_order_d = []

  # Iterate over all integers from 0 to p - 1.
  for i in range(p):

    # If the integer is of order d mod p, add it to the list.
    if order_of_integer(i, d, p) == d:
      integers_of_order_d.append(i)

  return integers_of_order_d
