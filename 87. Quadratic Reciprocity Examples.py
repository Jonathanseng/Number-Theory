def quadratic_reciprocity_examples():
  """
  Prints out some examples of the Quadratic Reciprocity.
  """


  print("The Legendre symbol of 2 modulo 3 is 1:")
  print(quadratic_reciprocity(2, 3))

  print("The Legendre symbol of 2 modulo 5 is -1:")
  print(quadratic_reciprocity(2, 5))

  print("The Legendre symbol of 3 modulo 4 is 1:")
  print(quadratic_reciprocity(3, 4))

  print("The Legendre symbol of 4 modulo 7 is -1:")
  print(quadratic_reciprocity(4, 7))

if __name__ == "__main__":
  quadratic_reciprocity_examples()
