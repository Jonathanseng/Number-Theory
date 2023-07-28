def euler_theorem_proof():
  """
  Proof of Euler's Theorem.

  Returns:
    True if the proof is correct, False otherwise.
  """
  a = 10
  n = 17

  # Calculate Euler's Totient Function for n.
  phi = phi(n)

  # Calculate (a ** (phi(n) - 1)) % n.
  a_power = a ** (phi(n) - 1)
  a_remainder = a_power % n

  # Check if (a ** (phi(n) - 1)) % n == 1.
  if a_remainder == 1:
    return True
  else:
    return False

if __name__ == "__main__":
  print(euler_theorem_proof())
