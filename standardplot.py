# Another sample file, this time teaching the installation of modules and using them
import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 20, 100) # Create a list of evenly-spaced numbers of the range
plt.plot(x, np.sin(x))      # Plot the sine of each x point
plt.show()                  # Display the plot