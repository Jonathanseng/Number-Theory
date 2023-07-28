def sums_of_squares_part7(n):
  """Returns a list of all sums of squares from 1 to n."""
  sums = []
  for i in range(1, n + 1):
    sum_of_squares = 0
    for j in range(1, i + 1):
      sum_of_squares += j ** 2
    sums.append(sum_of_squares)
  return sums

if __name__ == "__main__":
  for sum_of_squares in sums_of_squares_part7(10):
    print(sum_of_squares)
