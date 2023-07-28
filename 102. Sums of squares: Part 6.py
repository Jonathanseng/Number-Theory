from itertools import combinations

def sums_of_squares_part6(n):
  """Returns a list of all sums of squares from 1 to n."""
  sums = []
  for k in range(2, n + 1):
    for s in combinations(range(1, k + 1), k - 1):
      sums.append(sum(x * x for x in s))
  return sums

if __name__ == "__main__":
  for sum in sums_of_squares_part6(10):
    print(sum)
