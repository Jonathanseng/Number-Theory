def order_of_element_mod_n_proposition_2(a, n):
  """
  Calculates the order of an element modulo n using Proposition 2.

  Args:
    a: The element to calculate the order of.
    n: The modulus.

  Returns:
    The order of a modulo n.
  """

  # Calculate the order of a modulo n.
  order = order_of_integer_modulo_n(a, n)

  # If order is not equal to phi(n), then a is not a primitive root modulo n.
  if order != phi(n):
    return -1

  # Otherwise, a is a primitive root modulo n and the order is phi(n).
  return phi(n)

if __name__ == "__main__":
  a = 2
  n = 17
  print("The order of {} modulo {} using Proposition 2 is {}".format(a, n, order_of_element_mod_n_proposition_2(a, n)))
