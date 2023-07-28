def is_5_a_perfect_square_in_mod_p(p):
  """
  Checks if 5 is a perfect square modulo p.

  Args:
    p: The modulus.

  Returns:
    True if 5 is a perfect square modulo p, False otherwise.
  """

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  if p % 4 == 1:
    return True
  else:
    return False

def main():
  p = 5

  is_5_a_perfect_square_result = is_5_a_perfect_square_in_mod_p(p)

  print("5 is a perfect square modulo p:")
  print(is_5_a_perfect_square_result)

if __name__ == "__main__":
  main()
