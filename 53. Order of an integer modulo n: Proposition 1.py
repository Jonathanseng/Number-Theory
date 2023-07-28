def order_of_integer_modulo_n(a, n):
  """
  Calculates the order of an integer modulo n.

  Args:
    a: The integer to calculate the order of.
    n: The modulus.

  Returns:
    The order of a modulo n.
  """

  # Initialize the order.
  order = 0

  # Iterate from 1 to n.
  for i in range(1, n + 1):

    # If a ** i is 1 modulo n, then the order is i.
    if (a ** i) % n == 1:
      order = i
      break

  # Return the order.
  return order

if __name__ == "__main__":
  a = 10
  n = 17
  print("The order of {} modulo {} is {}".format(a, n, order_of_integer_modulo_n(a, n)))
