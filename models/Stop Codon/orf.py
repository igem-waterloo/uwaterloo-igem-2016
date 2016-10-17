

def get_orf(seq):
    pot_reading_frames = []
    sequence = []
    reading_frames = []
    i = 0
    while i < len(seq): #this part of the function finds the position of all start codons
        new_string = seq[i:len(seq)]
        start = "atg"
        index_of_starts = (new_string.find(start))
        i += 1
        if index_of_starts == 0:
            pot_reading_frames.append(i-1)
    for ind in pot_reading_frames:
        sequence.append(seq[ind:len(seq)])
    end = ["tag","tga", "taa"] #these are the stop codons where the protein would end
    for codon in end:
        for RF in sequence:
            index_of_end = RF.find(codon) #this loop cycles through the stop codons and finds the index of them
            if index_of_end % 3 == 0:
                reading_frames.append(RF[0:index_of_end+3])
    return reading_frames
