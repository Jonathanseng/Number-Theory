def gauss_lemma(n, p):
  """
  Checks if the congruence nx ≡ 1 (mod p) has a solution.

  Args:
    n: The number.
    p: The modulus.

  Returns:
    True if the congruence has a solution, False otherwise.
  """

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  if n == 0:
    return True

  g = 2
  while g * g <= p:
    if pow(g, (p - 1) // 2, p) == n:
      return True
    g += 1

  return False

def main():
  n = 3
  p = 5

  has_solution_result = gauss_lemma(n, p)

  print("The congruence nx ≡ 1 (mod p) has a solution:")
  print(has_solution_result)

if __name__ == "__main__":
  main()
