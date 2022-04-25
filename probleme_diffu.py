import numpy as np
import matplotlib.pyplot as plt



# PHYSICAL PARAMETERS
K = 0.5    #Diffusion coefficient
Lx = 1.0   #Domain size x
Ly = 1.0   #Domain size y
Time = 0.4 #Integration time
S = 0  #Source term

# NUMERICAL PARAMETERS

NT = 2000      #Number of time steps
NX = 50        #Number of grid points in x
NY = 50        #Number of grid points in y
dt = Time/NT   #Grid step (time)
dx = Lx/(NX-1) #Grid step in x (space)
dy = Ly/(NY-1) #Grid step in y (space)

xx = np.linspace(0,Lx,NX)
yy = np.linspace(0,Ly,NY)


plt.figure()

### MAIN PROGRAM ###

T = np.zeros((NX,NY))
RHS = np.zeros((NX,NY))
T[:,0] = 1000

# Main loop
for n in range(0,NT):
   RHS[1:-1,1:-1] = dt*K*( (T[:-2,1:-1]-2*T[1:-1,1:-1]+T[2:,1:-1])/(dx**2)
                         + (T[1:-1,:-2]-2*T[1:-1,1:-1]+T[1:-1,2:])/(dy**2) )
   T[1:-1,1:-1] += (RHS[1:-1,1:-1]+dt*S)


#Plot every 100 time steps
   if (n == 1900):
      plt.figure(1)
      plt.pcolormesh(T, cmap ='Oranges', vmin = 0, vmax = 1000)
      plt.axis('image')
      plt.draw()
      #plt.colorbar()


plt.show()

