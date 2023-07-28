def number_of_quadratic_residues(p):
  """
  Counts the number of quadratic residues modulo p.

  Args:
    p: The modulus.

  Returns:
    The number of quadratic residues modulo p.
  """

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  count = 0

  g = 2
  while g * g <= p:
    if is_quadratic_residue(g, p):
      count += 1
    g += 1

  return count

def main():
  p = 7
  number_of_quadratic_residues_result = number_of_quadratic_residues(p)

  print("The number of quadratic residues modulo p:")
  print(number_of_quadratic_residues_result)

if __name__ == "__main__":
  main()
