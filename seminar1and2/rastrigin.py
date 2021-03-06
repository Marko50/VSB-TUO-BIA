# The Rastrigin function has several local minima. 
# It is highly multimodal, but locations of the minima are regularly distributed.
import numpy as np

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X_mesh, Y_mesh = np.meshgrid(X, Y)

d = 2

sum_sq_term = X_mesh*X_mesh + Y_mesh*Y_mesh - 10*np.cos(d*np.pi*X_mesh) - 10*np.cos(d*np.pi*Y_mesh)

Z = sum_sq_term + 10*d