def lagrange_coefficient(f, x, s):
  """Returns the Lagrange coefficient of x and s for polynomial f."""
  n = len(f)
  result = 1
  for i in range(n):
    if i != s:
      result *= (x - s[i]) / (s[i] - s[s])
  return result

def lagrange_interpolation(f, s, x):
  """Returns the value of f(x) evaluated at x using Lagrange interpolation."""
  n = len(s)
  result = 0
  for i in range(n):
    result += f[i] * lagrange_coefficient(f, x, s)
  return result

def main():
  f = [1, 2, 3, 4, 5]
  s = [0, 1, 2, 3, 4]
  x = 2.5
  result = lagrange_interpolation(f, s, x)
  print(result)

if __name__ == "__main__":
  main()
