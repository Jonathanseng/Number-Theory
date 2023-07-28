def nonlinear_diophantine_equations(n):
  """Returns a list of all nonlinear Diophantine equations without solutions up to n."""
  equations = []
  for i in range(2, n):
    if i % 2 == 0:
      continue
    for j in range(2, n):
      if j % 2 == 0:
        continue
      equation = str(i) + "x^2 + " + str(j) + "y^2 = 1"
      if not is_diophantine_equation_solvable(equation):
        equations.append(equation)
  return equations

def is_diophantine_equation_solvable(equation):
  """Returns True if the Diophantine equation is solvable, False otherwise."""
  try:
    solver = DiophantineEquationSolver(equation)
    solver.solve()
    return True
  except ValueError:
    return False

if __name__ == "__main__":
  for equation in nonlinear_diophantine_equations(100):
    print(equation)
