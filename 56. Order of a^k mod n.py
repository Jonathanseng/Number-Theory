def order_of_a_k_mod_n(a, k, n):
  """
  Calculates the order of a^k modulo n.

  Args:
    a: The number to calculate the order of.
    k: The exponent.
    n: The modulus.

  Returns:
    The order of a^k modulo n.
  """

  # Initialize the order.
  order = 1

  # Iterate from 1 to k.
  for i in range(1, k + 1):

    # If a ** i is 1 modulo n, then the order is i.
    if (a ** i) % n == 1:
      order = i
      break

  # Return the order.
  return order

if __name__ == "__main__":
  a = 2
  k = 10
  n = 17
  print("The order of {}^{} modulo {} is {}".format(a, k, n, order_of_a_k_mod_n(a, k, n)))
