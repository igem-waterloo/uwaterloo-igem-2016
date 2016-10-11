
# coding: utf-8

# Imports

# In[10]:

# Imports
import numpy as np
import random
import math
import matplotlib.pyplot as plt


# Parameter values

# In[27]:

transmission_threshold = 20
max_age = 25


# Useful functions

# In[53]:

def remove_empty(x):
    i = 0
    while i < x.shape[0]:
        if x[i][1] == 0:
            x = np.delete(x, (i), axis=0)
        else:
            i += 1
    return(x)


# In[56]:

amyloids = np.array([[1,0],[2,0],[3,5],[4,7],[6,0],[7,10],[8,0]])
print(amyloids)
print()
print(remove_empty(amyloids))


# Yeast cell class

# In[3]:

class Cell(object):

    # Class initialization
    def __init__(self, cells, sup35, amyloids, age = 1):
        self.cells = cells       # list of cells
        self.sup35 = sup35       # amount of healthy sup35
        self.amyloids = amyloids # list of amyloid sizes and number at that size
        self.age = age           # generation of cell
    
    # When a cell buds, it creates two cells
    def bud(self):
        # -- Determine what to pass to daughter
        prob_passing = 0.4
        # How much healthy sup35 to pass
        daughter_sup35 = np.random.binomial(self.sup35,prob_passing)
        # How many size classes there are
        num_classes = self.amyloids.shape[2]
        # Create vector to hold how many amyloids transmit to the daughter
        daughter_amyloids = np.zeros(num_classes)
        # Randomly distribute small amyloids to the daughter cells
        for i in range(len(self.amyloids)):
            if self.p
            # Determine how many amyloids will pass to the daughter
            num_amyloids = self.small_amyloids[i]
            daughter_amyloids[i] = np.random.binomial(num_amyloids,prob_passing)
            break
            
        # -- Update both cells
        # Create daughter cell with above small amyloid distribution
        self.cells.append(Cell(cells, np.random.binomial(self.sup35,prob_passing), daughter_amyloids, []))
        # Update mother cell
        self.small_amyloids -= daughter_amyloids
        self.age += 1
    
    # Approximate SSA for binding of amyloids, hsp104 corrections, and sup35 misfolding
    def aggregation(self):
        # The number of amyloids at the start of the time step
        num_amyloids = np.sum(self.small_amyloids) + len(self.large_amyloids)
        
        # -- Constants
        generation_time = 2. # two hours between budding events
        bind_rate = 0.001
        
        # -- Main loop
        time = 0
        while time < generation_time:
            
            # -- Determine which molecules will react next
            # Number of molecules available for reaction
            num_amyloids = np.sum(self.small_amyloids) + len(self.large_amyloids)
            # Select two molecules to react
            mol = np.sort(random.sample(range(num_amyloids),2))
            
            # -- Determine when the reaction will occur
            # Propensity for a reaction to occur
            prop_bind = bind_rate * num_amyloids*(num_amyloids-1)
            # Time between events (assumed to be Poisson distributed)
            r = random.random() # random number in [0,1)
            tau = -math.log(r)/prop_bind
            
            # -- Simulation of reaction
            # Index of first molecule
            size = 1
            if mol[1] < np.sum(self.small_amyloids):
                size = 1
                while mol[1] > np.sum(self.small_amyloids[0:size]):
                    size += 1
                ind = size-1
            else:
                
            
            
            


# Function to cause all cells to bud

# In[26]:

bind_rate = 0.001
num_amyloids = 100

prop_bind = bind_rate * num_amyloids*(num_amyloids-1)
r = random.random()
tau = -math.log(r)/prop_bind
print(tau)
mol = np.sort(random.sample(range(num_amyloids),2))
print(mol)

vec = random.sample(range(100),5)
ind = 1
vec[0:ind]
#np.sum(vec[0:ind])


# In[8]:

def bud_event(cells):
    for cell in cells:
        cell.bud()


# Parameter values

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



