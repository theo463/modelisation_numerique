import numpy as np
import matplotlib.pyplot as plt

from scipy.linalg import block_diag

# PHYSICAL PARAMETERS
K = 0.5    #Diffusion coefficient
Lx = 1.0   #Domain size x
Ly = 1.0   #Domain size y


# NUMERICAL PARAMETERS®


NX = 5    #Number of grid points in x
NY = 5     #Number of grid points in y

dx = Lx/(NX-1) #Grid step in x (space)
dy = Ly/(NY-1) #Grid step in y (space)

xx = np.linspace(0,Lx,NX)
yy = np.linspace(0,Ly,NY)



T = (-2*((1/dx)**2 + (1/dy)**2))*np.eye(NX-2) + (1/dx)**2 *np.eye(NX-2, k=1) + (1/dx)**2 *np.eye(NX-2, k=-1)
I = (1/dy)**2 * np.eye(NY-2)

num_block = NY

UP = np.eye(num_block,num_block, k =1)
DOWN = np.eye(num_block,num_block, k =-1)
MIDLE = np.eye(num_block,num_block)

A = (np.kron(UP, I) + np.kron(MIDLE, T) + np.kron(DOWN, I))

















