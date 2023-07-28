def sums_of_squares(n):
  """Returns a list of all sums of squares from 1 to n."""
  sums = []
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      sums.append(i * i + j * j)
  return sums

if __name__ == "__main__":
  for sum in sums_of_squares(10):
    print(sum)
