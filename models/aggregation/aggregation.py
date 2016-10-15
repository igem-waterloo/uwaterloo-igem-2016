
# coding: utf-8

# In[1]:

# -- Imports

import numpy as np
import random
import math
import matplotlib.pyplot as plt


# In[2]:

# -- Parameter values

transmission_threshold = 20
prob_passing = 0.4
max_age = 25


# In[3]:

# -- Useful functions

# Given a list of amyloids, remove unused size classes
def remove_empty(x):
    i = 0
    while i < x.shape[0]:
        if x[i][1] == 0:
            x = np.delete(x, (i), axis=0)
        else:
            i += 1
    return(x)

# Determine the total number of amyloids
def sum_amyloids(x):
    a = 0
    for i in range(x.shape[0]):
        a += x[i][1]
    return(a)

# Randomly select an amyloid to be involved in a reaction
def find_decr_size(x):
    a = sum_amyloids(x)
    r = random.uniform(0, a)
    count = 0
    for i in range(x.shape[0]):
        if count + x[i][1] > r:
            return(x[i][0])
        count += x[i][1]

# Decrement a given size class
def decr(x,size):
    ind = np.where(x[:,0]==size)[0][0]
    if x[ind][1] == 1:
        x = np.delete(x, (ind), axis=0)
    else:
        x[ind][1] -= 1
    return(x)

# Increment a given size class
def incr(x,size):
    if size in x[:,0]:
        ind = np.where(x[:,0]==size)[0][0]
        x[ind][1] += 1
    else:
        np.append(x,np.array([size,1]))
    return(x)


# In[4]:

# -- Definition of cell

class Cell(object):

    # Class initialization
    def __init__(self, cells, sup35, amyloids, age = 1):
        self.cells = cells       # list of cells
        self.sup35 = sup35       # amount of healthy sup35
        self.amyloids = amyloids # list of amyloid sizes and number at that size
        self.age = age           # generation of cell
    
    # When a cell buds, it creates two cells
    def bud(self):
        
        # Split healthy sup35 between cells
        daughter_sup35 = np.random.binomial(self.sup35,prob_passing)
        mother_sup35 = self.sup35 - daughter_sup35
        
        # Create vector to hold how many amyloids transmit to the daughter
        daughter_amyloids = np.copy(self.amyloids)
        mother_amyloids = np.copy(self.amyloids)
        
        # Randomly distribute small amyloids to the daughter cells
        for i in range(len(daughter_amyloids[:,0])):
            if self.amyloids[i][0] <= transmission_threshold:
                num_amyloids = self.amyloids[i][1]
                daughter_amyloids[i][1] = np.random.binomial(num_amyloids,prob_passing)
                mother_amyloids[i][1] -= daughter_amyloids[i][1]
            else:
                daughter_amyloids[i][1] = 0
            
        # Create daughter cell with above small amyloid distribution
        self.cells.append(Cell(cells, daughter_sup35, remove_empty(daughter_amyloids)))
        
        # Update mother cell
        self.sup35 = mother_sup35
        self.amyloids = remove_empty(mother_amyloids)
        self.age += 1
        
    
    # Gillespie algorithm for binding of amyloids, hsp104 corrections, and sup35 misfolding
    def gillespie(self):
        
        # Constants
        generation_time = 2. # two hours between budding events
        
        # Initial state of cell
        s = self.sup35                  # amount of sup35
        a = sum_amyloids(self.amyloids) # total number of aggregates/misfolded protein
        ams = self.amyloids
        
        # Main loop
        t = 0.
        ind = 0
        
        # Arrays to hold output over time
        t_array = np.array([t])
        s_array = np.array([self.sup35])
        #ams_array = np.array([self.amyloids])
        ams_next = self.amyloids
        
        while t < generation_time:
            
            s = s_array[ind]
            #ams = ams_array[ind]
            ams = ams_next
            a = sum_amyloids(ams)
            
            # Rate constants
            rate_prod = 0.02
            rate_degr = 0.01
            rate_conv = 0.01
            rate_inft = 0.01
            rate_cure = 0.01
            rate_bind = 0.01
            
            # Compute propensities for reactions
            prop_prod = rate_prod           # Production of sup35
            prop_degr = rate_degr * s       # Degradation of sup35
            #prop_conv = rate_conv * s      # Spontaneous conversion of healthy sup35 to infectious
            prop_conv = 0                   # Assume misfolding is rare enough to be negligible
            prop_inft = rate_inft * s*a     # Infection of healthy sup
            prop_cure = rate_cure * a       # Curing of infectious sup35 by hsp104
            prop_bind = rate_bind * a*(a-1) # Aggregation of infectious sup35
            
            # Total propensity
            prop = prop_prod + prop_degr + prop_conv + prop_inft + prop_cure + prop_bind
            
            # Determine when next reaction will occur
            r1 = random.random() # random number in [0,1)
            dt = -math.log(r1)/prop
            
            # Determine which reaction occurs next
            r2 = random.uniform(0,prop)
            prop_array = [prop_prod, prop_degr, prop_conv, prop_inft, prop_cure, prop_bind]
            prop_cdf = np.cumsum(prop_array)
            
            # Update molecule numbers
            if r2 < prop_cdf[0]:
                # create sup35
                s += 1
                event = "sup35+"
            elif r2 < prop_cdf[1]:
                # degrage sup35
                s -= 1
                event = "sup35-"
            elif r2 < prop_cdf[2]:
                # spontaneously convert sup35 to infectious
                # this almost never happens so I won't code it
                s += 0
                event = "spontaneous"
            elif r2 < prop_cdf[3]:
                # attach healthy sup35 to aggregate
                s -= 1
                size_decr = find_decr_size(ams) # randomly select molecule to decrement
                ams = decr(ams, size_decr)      # decrease molecule count by one
                ams = incr(ams, size_decr+1)    # increase molecule count by one
                event = "added sup35"
            elif r2 < prop_cdf[4]:
                # cure infected sup35
                size_decr = find_decr_size(ams)
                ams = decr(ams, size_decr)
                event = "cure"
            elif r2 < prop_cdf[5]:
                # combine two amyloids
                size_decr1 = find_decr_size(ams)
                ams = decr(ams, size_decr1)
                size_decr2 = find_decr_size(ams)
                ams = decr(ams, size_decr2)
                ams = incr(ams, size_decr1+size_decr2)
                event = "bind"
            
            # Update time
            t += dt
            #print(t, event)
            
            # Update index
            ind += 1
            
            # Append things to other things
            t_array = np.append(t_array,t)
            s_array = np.append(s_array,s)
            ams_next = np.copy(ams)
            #ams_array = np.append(ams_array,ams,axis=0)
        
        self.sup35 = s
        self.ams = ams


# In[5]:

# -- Functions that perform a step for each cell

# Cause all cells to bud at 2 hours
def bud_event(cells):
    num_cells = len(cells)
    for i in range(num_cells):
        cells[i].bud()

# Run Gillespie's algorithm for 2 hours in between budding
def run_gillespie(cells):
    num_cells = len(cells)
    for i in range(num_cells):
        cells[i].gillespie()


# In[6]:

# -- Function to evaluate state of cells

def enumerate_cells(cells):
    num_cells = len(cells)
    num_psi = 0
    for cell in cells:
        num_amyloids = sum_amyloids(cell.amyloids)
        if num_amyloids > 10:
            num_psi += 1
    return(num_psi)


# In[7]:

# -- Run simulation

# Initial condition
cells = []
init_sup35 = 1000
init_amyloids = np.array([[1,500],[2,350],[3,210],[4,150],[6,90],[7,20],[12,10]])
cells.append(Cell(cells, init_sup35, init_amyloids))

# Number of generations to simulate
num_gen = 10

# Maximum number of cells to keep track of
max_cells = 2**8 # only track 256 cells

# Loop through
for i in range(num_gen):
    
    # Simulate budding and aggregation dynamics
    run_gillespie(cells)
    bud_event(cells)
    
    # Limit the number of cells to "max_cells"
    if len(cells) > max_cells:
        cells = cells
    
    # Count how many cells there are
    num_cells = len(cells)
    num_psi = enumerate_cells(cells)
    print(num_psi,num_cells, 100.*num_psi/num_cells)


# In[8]:

# -- LIST OF TESTS TO PERFORM

# Test the five helper functions
#  remove_empty
#  sum_amyloids
#  find_decr_size
#  decr
#  incr

# Budding
#  New cell is created properly
#  Distribution of sup35 and amyloids works properly

# Gillespie algorithm
#  


# In[9]:

# TEST

# Create cell
cells = []
init_sup35 = 100
init_amyloids = np.array([[1,50],[2,35],[3,21],[4,15],[6,9],[7,2],[8,1]])
cells.append(Cell(cells, init_sup35, init_amyloids))


# In[10]:

# Test Gillespie algorithm
cells[0].gillespie()


# In[11]:

# Test cell specification
print("Test cell specs")
print("sup35", cells[0].sup35)
print("amyloids", cells[0].amyloids)
print("age", cells[0].age)
print("count", len(cells))


# In[12]:

# Test budding
cells[0].bud()
print("Test budding")
print("sup35", cells[0].sup35)
print("amyloids", cells[0].amyloids)
print("age", cells[0].age)
print("sup35-d", cells[1].sup35)
print("amyloids-d", cells[1].amyloids)
print("age-d", cells[1].age)
print("count", len(cells))


# In[13]:

# Test that the functions in the third block work
amyloids = np.array([[1,50],[2,35],[3,21],[4,15],[6,9],[7,2],[8,1]])
n = 13300
temp = np.zeros(n)
#print temp
for i in range(n):
    temp[i] = find_decr_size(amyloids)
    
#print temp
print(1, len(np.where(temp==1)[0]))
print(2, len(np.where(temp==2)[0]))
print(3, len(np.where(temp==3)[0]))
print(4, len(np.where(temp==4)[0]))
print(5, len(np.where(temp==5)[0]))
print(6, len(np.where(temp==6)[0]))
print(7, len(np.where(temp==7)[0]))
print(8, len(np.where(temp==8)[0]))


# In[14]:

# Test all bud
print("count", len(cells))
bud_event(cells)
print("count", len(cells))
bud_event(cells)
print("count", len(cells))
bud_event(cells)
print("count", len(cells))


# In[ ]:




# In[ ]:



