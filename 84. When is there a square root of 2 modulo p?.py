def has_square_root_of_2_modulo_p(p):
  """
  Checks if there exists a square root of 2 modulo p.

  Args:
    p: The modulus.

  Returns:
    True if there exists a square root of 2 modulo p, False otherwise.
  """

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  if p % 4 == 3:
    return True
  else:
    return False

def main():
  p = 5

  has_square_root_result = has_square_root_of_2_modulo_p(p)

  print("There exists a square root of 2 modulo p:")
  print(has_square_root_result)

if __name__ == "__main__":
  main()
