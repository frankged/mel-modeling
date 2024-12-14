import numpy as np
#this will be a holder for the functions that exist

#basic symmetric growth model, i.e. given some delta_t
#params: delta_t, D = Diffusivity, c = coarse-graining/particle size, grid_size = N^2
def diffusion(delta_t, D, c, grid, delta_x):
    #this is a random walk of packets of fluid of size c
    # Generate 100 samples from a Gaussian distribution with mean 0 and standard deviation 1
    # sigma = np.sqrt(2*D*delta_t)
    # samples = np.random.normal(loc=0, scale=sigma, size=grid_size*c)
    # print(samples)
    dummy = np.zeros((grid.size,grid.size))
    for i in range(grid.size):
        for j in range(grid.size):
            dummy[i][j] = diffusion_update_square(i,j,grid.array,delta_t,delta_x,grid.size)
    grid.array = dummy
    return grid
            

def diffusion_update_square(i,j, T, delta_t,delta_x, N):
    h = delta_x
    #Need boundary conditions for i = 0,N or j = 0,N
    #setting boundary to 0
    if i == 0 or j == 0 or i == N - 1 or j == N - 1:
        return 0
    A = T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1] - 4*T[i][j]
    T_new = T[i][j] + delta_t/h**2 *A
    return T_new

#this is not really working, particularly to the extent that there is a size-exclusion
#property in the skin that creates outward pressure
def diffusion_plus_growth(delta_t, D, c, grid, delta_x):
    growth_rate = 0.2
    dummy = np.zeros((grid.size,grid.size))
    for i in range(grid.size):
        for j in range(grid.size):
            dummy[i][j] = diffusion_growth_update_square(i,j,grid.array,delta_t,delta_x,grid.size, growth_rate)
    grid.array = dummy
    return grid

def diffusion_growth_update_square(i,j, T, delta_t,delta_x, N, growth_rate):
    h = delta_x
    #Need boundary conditions for i = 0,N or j = 0,N
    #setting boundary to 0
    if i == 0 or j == 0 or i == N - 1 or j == N - 1:
        return 0
    A = T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1] - 4*T[i][j]
    #this is the only difference from diffusion
    A += growth_rate*T[i][j]
    T_new = T[i][j] + delta_t/h**2 *A
    return T_new


#basic symmetric growth model, i.e. given some delta_t, each 
#params: delta_t, growth_per_cell
# def symm_growth(delta_t, growth_per_cell):
    #based on delta_t, and growth_per_cell, we s

# diffusion(0.4,1)



#Paper 1
#Balois, T., Amar, M. Morphology of melanocytic lesions in situ. Sci Rep 4, 3622 (2014). https://doi.org/10.1038/srep03622
def mmlinsitu_update_square(i,j,T,delta_t,delta_x,N,kappa=0,beta=0.2,phi=0.6):
    h = delta_x
    #Need boundary conditions for i = 0,N or j = 0,N
    #setting boundary to 0
    if i == 0 or j == 0 or i == N - 1 or j == N - 1:
        return 0
    A = T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1] - 4*T[i][j]
    B = -kappa*(1-phi)*T[i][j] - T[i][j]*phi + beta*(1 - T[i][j])
    #this is the only difference from diffusion
    # A += growth_rate*T[i][j]
    T_new = A*delta_t/delta_x + B
    return T_new

def mmlinsitu(delta_t, D, c, grid, delta_x):
    dummy = np.zeros((grid.size,grid.size))
    for i in range(grid.size):
        for j in range(grid.size):
            dummy[i][j] = mmlinsitu_update_square(i,j,grid.array,delta_t,delta_x,grid.size)
    grid.array = dummy
    return grid