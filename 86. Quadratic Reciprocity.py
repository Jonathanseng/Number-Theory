def quadratic_reciprocity(p, q):
  """
  Calculates the Legendre symbol of p modulo q using quadratic reciprocity.

  Args:
    p: The number.
    q: The modulus.

  Returns:
    The Legendre symbol of p modulo q.
  """

  if p == 0:
    return 0

  if not is_prime(p):
    raise ValueError("p is not a prime number")
  
  if not is_prime(q):
    raise ValueError("q is not a prime number")

  if q % 2 == 0:
    if p % 4 == 1:
      return 1
    else:
      return -1
  else:
    if p % 4 == 1:
      if q % 4 == 1:
        return 1
      else:
        return -1
    else:
      if q % 4 == 1:
        return -1
      else:
        return 1

def main():
  p = 2
  q = 3

  legendre_symbol_result = quadratic_reciprocity(p, q)

  print("The Legendre symbol of p modulo q:")
  print(legendre_symbol_result)

if __name__ == "__main__":
  main()
