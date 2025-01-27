import numpy as np
import matplotlib.pyplot as plt

# Define constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
M_sun = 1.9885e30  # Mass of the Sun in kg
AU_to_m = 1.496e11  # Conversion factor from AU to meters
seconds_per_year = 3.154e7  # Number of seconds in a year

# Define orbital elements
a = 3.540  # Semi-major axis in AU
e = 0.4072  # Eccentricity

b = a * np.sqrt(1 - e**2)  # Semi-minor axis in AU

# Distance from the center to the focus
c = a * e

# Aphelion and Perihelion
aphelion = a * (1 + e)
perihelion = a * (1 - e)

# Major axis
major_axis = 2 * a

# Print the aphelion, perihelion, and major axis
print(f"Aphelion: {aphelion:.2f} AU") # 2 d.p
print(f"Perihelion: {perihelion:.4f} AU") # 4 d.p
print(f"Major axis: {major_axis:.2f} AU") # 2 d.p

# Convert semi-major axis from AU to meters for orbital period calculation
a_meters = a * AU_to_m

# Calculate orbital period in seconds using the formula
orbital_period_seconds = np.sqrt(4 * np.pi**2 * a_meters**3 / (G * M_sun))

# Convert orbital period from seconds to years
orbital_period_years = orbital_period_seconds / seconds_per_year

# Print the orbital period
print(f"Orbital period: {orbital_period_years:.4f} years")

# Define the range of true anomaly
theta = np.linspace(0, 2 * np.pi, 1000)

# Calculate the radius for each theta
r = (a * b) / np.sqrt(a**2 - c**2 * np.cos(theta)**2)

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the orbit
plt.figure(figsize=(10, 10))
# Plot with x+c in order to make the Sun the left focus
plt.plot(x + c, y, label="Orbit")
plt.plot(0, 0, 'yo', label='Sun')  # Sun at the origin

# Highlight perihelion and aphelion
plt.plot(aphelion, 0, 'ro', label='Aphelion')
plt.plot(-perihelion, 0, 'bo', label='Perihelion')

plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title("Orbit")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
