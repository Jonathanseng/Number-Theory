def solve_linear_congruence(a, b, m):
  """Returns all solutions to the linear congruence ax ≡ b (mod m)."""
  gcd = math.gcd(a, m)
  if b % gcd != 0:
    return []
  else:
    u, v = _extended_euclidean_algorithm(a, m)
    solutions = []
    for i in range(gcd):
      solutions.append((u * i * b) // gcd % m)
    return solutions

def _extended_euclidean_algorithm(a, b):
  """Returns the tuple (u, v) such that au + bv = gcd(a, b)."""
  if b == 0:
    return (1, 0)
  else:
    u, v = _extended_euclidean_algorithm(b, a % b)
    return (v, u - (a // b) * v)

def main():
  a = 7
  b = 10
  m = 12
  solutions = solve_linear_congruence(a, b, m)
  print(solutions)

if __name__ == "__main__":
  main()
