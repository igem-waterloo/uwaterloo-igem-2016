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

effects = [
    ("CGGA",(1,2,3,5),0.35),
    ("CCCA",(1,2,4,6),0.45),
    ("CC", (-1,-2),0.45),
    ("CGA",(3,4,5),0.4)]

suitability_rating = [0.0]

frame = "CCCCCAAGCACG"
position = 0
max_suitability = 0.0
#Iterate through the 
for position in range(0, len(frame), 3):
    #print ("Evaluating suitability of position: ", position)
    suitability_rating.append(0.0)
    for j in effects:
        #print("Testing effect of context: ", j)
        current_letter = 0
        satisfies_context = True
        #Check the surrounding frame at the correct position for each of the letters in the context. 
        #Flag if there are any mismatches.
        for letter in j[0]:
            try:
                if frame[position + j[1][current_letter]] != letter:
                    satisfies_context = False
            except:
                #print("Failed to find context!")
                #print("Suitability for position ", position, " remains ", suitability_rating[position/3])
                satisfies_context = False
            current_letter += 1
        #If no mismatches were flagged, up the suitability rating accordingly.
        if satisfies_context:
            suitability_rating[int(position/3)] += (j[2])
            #print("Match found for ", j[0], "! Suitability rating for position: ",position, " is: ", suitability_rating[position/3])
    print("Overall suitability for position ",position," is ", suitability_rating[int(position/3)])
    max_suitability = max(suitability_rating[int(position/3)], max_suitability)

print( "The order of suitability is: ", (sorted(enumerate(suitability_rating), key=lambda x: x[1]))[::-1])
#print("The most suitable position is ", (suitability_rating.index(max_suitability))*3, " with a rating of ", max_suitability, ".") #"The best position is ", best_position, "!")
