from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import functions

#Create a 2D Grid environment. 
class Grid2D:
    #initalize 2D Grid(size = N) of dimensions NxN
    def __init__(self,size):
        self.size = size
        self.array = np.zeros((size,size))

    #some kind of way to fill our array to a starting position
    # def fill(oldarray):


    def draw_vline(self, x):
        self.array[50][x] = 1.0
        self.array[51][x] = 1.0
        self.array[52][x] = 1.0
        self.array[53][x] = 1.0
        self.array[54][x] = 1.0
        self.array[55][x] = 1.0
        self.array[56][x] = 1.0
        self.array[57][x] = 1.0
        self.array[58][x] = 1.0
        self.array[59][x] = 1.0


    def draw_hline(self,y):
        self.array[y][50] = 1.0
        self.array[y][51] = 1.0
        self.array[y][52] = 1.0
        self.array[y][53] = 1.0
        self.array[y][54] = 1.0
        self.array[y][55] = 1.0
        self.array[y][56] = 1.0
        self.array[y][57] = 1.0
        self.array[y][58] = 1.0
        self.array[y][59] = 1.0

    #some kind of way to do a forwards time-step 
    #for each element of the array in a given model function
    # def step(delta_t, function):


    #display function on 2D color map from matplotlib
    def display(self):
        # Display the array as an image
        plt.imshow(self.array, cmap='viridis')  # 'viridis' is a colormap, choose any you like
        plt.colorbar()  # Add a colorbar to show values-to-color mapping
        plt.title("2D Array Visualization")
        plt.show()


    def animate(self, frames, func):
        # Generate synthetic data
        # Number of frames in the animation(frames)
        N = self.size
        grid = self
        rows, cols = N, N  # Dimensions of the grid
        data = [] # Time-varying 2D data
        for i in range(frames):
            dummy = func(0.1, 1, 1, grid, 1)
            data.append(dummy.array)
            grid = dummy

        # Set up the figure and axis
        fig, ax = plt.subplots()
        cax = ax.imshow(data[0], cmap='viridis', interpolation='nearest')
        fig.colorbar(cax)

        # Update function for animation
        def update(frame):
            cax.set_array(data[frame])  # Update the heatmap
            return [cax]

        # Create the animation
        ani = FuncAnimation(fig, update, frames=frames, blit=True, interval=100)

        # Show the animation
        plt.show()

#we can later adapt this to a 3D Grid environment


#Example of initialize and print array with basic manipulation
grid = Grid2D(100)
print(grid.array)
grid.draw_hline(50)
grid.draw_vline(50)
grid.draw_hline(40)
print(grid.array)
grid.display()

# grid.animate(100, functions.diffusion)
grid.animate(100, functions.diffusion_plus_growth)

# grid_update = functions.diffusion(1, 1, 1, grid, 1)

# for i in range(10):
#     grid_update = functions.diffusion(0.1, 1, 1, grid, 1)
#     print(grid_update.array)
#     grid_update.display()
#     grid = grid_update
    

