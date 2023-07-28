def gauss_theorem(surface, charge_density):
  """
  Calculates the electric flux through a surface using Gauss' Theorem.

  Args:
    surface: A list of triangles that define the surface.
    charge_density: The charge density on the surface.

  Returns:
    The electric flux through the surface.
  """

  # Calculate the area of each triangle.
  area = [triangle.area() for triangle in surface]

  # Calculate the electric flux through each triangle.
  flux = [charge_density * area for area in area]

  # Sum the electric flux through all of the triangles.
  return sum(flux)
