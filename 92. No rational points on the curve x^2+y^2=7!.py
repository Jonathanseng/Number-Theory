def is_rational_point_on_curve(x, y):
  """Returns True if (x, y) is a rational point on the curve x^2+y^2=7!, False otherwise."""
  if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
    return False
  if x % 4 == 3:
    return False
  return (x * x + y * y) % 720 == 0

if __name__ == "__main__":
  for x in range(-10, 10):
    for y in range(-10, 10):
      if is_rational_point_on_curve(x, y):
        print(x, y)
