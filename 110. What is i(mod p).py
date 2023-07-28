def i_mod_p(i, p):
  """Returns the remainder of i when divided by p."""
  if i < 0:
    i += p
  return i % p

def main():
  print(i_mod_p(5, 7))
  print(i_mod_p(-1, 7))

if __name__ == "__main__":
  main()
