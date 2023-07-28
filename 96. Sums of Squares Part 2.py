def sums_of_squares_part2(n):
  """Returns a list of all sums of squares from 1 to n."""
  sums = []
  for i in range(1, n + 1):
    sums.append(2 * i * (i - 1))
  return sums

if __name__ == "__main__":
  for sum in sums_of_squares_part2(10):
    print(sum)
