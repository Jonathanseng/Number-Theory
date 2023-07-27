def has_solution(a, b, m):
  """Returns True if the linear congruence ax ≡ b (mod m) has a solution, False otherwise."""
  gcd = math.gcd(a, m)
  if b % gcd != 0:
    return False
  else:
    return True

def main():
  a = 2
  b = 3
  m = 5
  print(has_solution(a, b, m))

if __name__ == "__main__":
  main()
