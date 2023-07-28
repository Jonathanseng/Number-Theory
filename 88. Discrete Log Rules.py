def discrete_log_rule_1(a, b, c, p):
  """
  Checks if the Discrete Log Rule 1 holds.

  Args:
    a: The base.
    b: The exponent.
    c: The modulus.

  Returns:
    True if the Discrete Log Rule 1 holds, False otherwise.
  """

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  if a == 0:
    return True

  if b == 0:
    return False

  if c == 0:
    return False

  if pow(a, b, c) == pow(a, c, c):
    return True
  else:
    return False

def discrete_log_rule_2(a, b, c, p):
  """
  Checks if the Discrete Log Rule 2 holds.

  Args:
    a: The base.
    b: The exponent.
    c: The modulus.

  Returns:
    True if the Discrete Log Rule 2 holds, False otherwise.
  """

  if not is_prime(p):
    raise ValueError("p is not a prime number")

  if a == 0:
    return False

  if b == 0:
    return True

  if c == 0:
    return False

  if pow(a, b, c) == pow(a, (b * c) % p, c):
    return True
  else:
    return False

def main():
  a = 2
  b = 3
  c = 5
  p = 7

  rule_1_result = discrete_log_rule_1(a, b, c, p)
  rule_2_result = discrete_log_rule_2(a, b, c, p)

  print("Rule 1 holds:")
  print(rule_1_result)

  print("Rule 2 holds:")
  print(rule_2_result)

if __name__ == "__main__":
  main()
