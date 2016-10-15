from math import *
from numpy import *

"""
Framework for evaluating the suitability of any particular stop codon
positioning in a frame.

TODO: -create list of contexts+effects to replace placeholder code
-create function to find open reading frame (find start codon, 
then have the frame begin there)
-all the testing

"""
"""
First element in sublists is the letters composing the context
Second element in sublists is the positioning of each letter. These MUST
be the same length
The third element is the relative effect of that context
"""
effects = [("CGGA",(1,2,3,5),0.35),
                  ("CCCA",(1,2,4,6),0.1),
                  ("CGA",(3,4,5),0.4)]

suitability = [(0)]

frame = "OPENREADINGFRAME"

for i in range(0,len(frame)/3):
    index = i*3
    suitability.append(0)
    for j in effects:
        for letter in j[1]:
            if frame(index + (j[2])[letter.index]) == letter:
                suitability += (j[3])
