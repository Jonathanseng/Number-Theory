def linear_congruence_proposition_2(a, b, m, n):
  """Returns True if the linear congruence ax ≡ b (mod m) has a solution
  that also satisfies x ≡ n (mod m), False otherwise."""
  gcd = math.gcd(a, m)
  if b % gcd != 0:
    return False
  else:
    return (n * gcd) % m == b % m

def main():
  a = 2
  b = 3
  m = 5
  n = 1
  print(linear_congruence_proposition_2(a, b, m, n))

if __name__ == "__main__":
  main()
