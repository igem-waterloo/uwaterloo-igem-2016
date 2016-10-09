
# coding: utf-8

# Imports

# In[2]:

# Import numpy
import numpy as np

# Import random
import random

# Import plotting library
import matplotlib.pyplot as plt


# Yeast cell class

# In[6]:

class Cell(object):

    # Class initialization
    def __init__(self, cells, small_amyloids, large_amyloids, age = 1):
        self.cells = cells                   # list of cells
        self.small_amyloids = small_amyloids # count of small amyloids in each size class
        self.large_amyloids = large_amyloids # list of amyloids too large to propagate
        self.age = age                       # generation of cell
    
    # When a cell buds, it creates two cells
    def bud(self):
        # Create vector to hold how many amyloids transmit to the daughter
        daughter_amyloids = np.zeros(len(self.small_amyloids))
        # Randomly distribute small amyloids to the daughter cells
        for i in range(len(self.small_amyloids)):
            # Determine how many amyloids will pass to the daughter
            prob_passing = 0.4
            num_amyloids = self.small_amyloids[i]
            daughter_amyloids[i] = np.random.binomial(num_amyloids,prob_passing)
        # Create daughter cell with above small amyloid distribution
        self.cells.append(Cell(cells, np.random.binomial(self.sup35,prob_passing), daughter_amyloids, []))
        # Update mother cell
        self.small_amyloids -= daughter_amyloids
        self.age += 1
    
    # Approximate SSA for binding of amyloids, hsp104 corrections, and sup35 misfolding
    def aggregation(self):
        # The number of amyloids at the start of the time step
        num_amyloids = np.sum(self.small_amyloids) + len(self.large_amyloids)
        # Estimate the number of binding events that occur between cell divisions
        generation_time = 2 # two hours between budding events
        tau_sub = 10        # update molecule concentration 10 times between budding events
        tau_time = generation_time./tau_sub # leap time
        bind_rate = 0.001
        while time < generation_time:
            # Propensity for a reaction to occur
            prop_bind = bind_rate * num_amyloids*(num_amyloids-1)
            # Time between events
            
            
            


# Function to cause all cells to bud

# In[8]:

def bud_event(cells):
    for cell in cells:
        cell.bud()


# Parameter values

# In[12]:

transmission_threshold = 20


# Initial conditions

# In[13]:

# Create one cell
cells = []
init_small_amyloids = np.zeros(transmission_threshold)
init_small_amyloids[0] = 10
cells.append(Cell(cells, init_small_amyloids, []))


# Main

# In[20]:

# Test
print(cells[0].age)


# In[14]:

plt.plot([1 - x for x in psi_minus_vals])
plt.ylabel('Psi+%')
plt.xlabel('Generation #')
plt.show()


# In[22]:

10./11


# In[ ]:



