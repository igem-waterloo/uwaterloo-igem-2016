"""
#####################################################################
Pseudocode for a stop codon identification programme
#####################################################################
Input: protein sequence, in frame
    - should eventually be a regular .txt file or .fasta file
    - should eventually be able to specify mutagenesis or de novo construction
Notes:
    - look back over best algorithms for searching (esp. 2 lists)
    - "Compare" section needs work to reduce code duplication
        - should create helper function to do actual comparison


## Search ##
Iterate through the given sequence (wnile not null)
    Keep a counter of the sequence position, seqPos
    Add the next letter to codon string
    If the length of codon == 3
        If codon == CAG
            Add seqPos to CAGmatches
        If codon == CAA
            # This is separate (not equivalent to CAGmatches) only if stop codon mutagenesis is used
            Add seqPos to CAAmatches
        If codon == TAG
            # Simplified - other factors play into the role of the +6nt
            If sequence + 6 == T or C
                Add seqPos to betterTAG
            Else
                Add seqPos to TAGmatches
        If codon == TAA
            # Simplified - other factors play into the role of the +6nt
            If sequence + 6 == T or C
                # Again, this is only different (from betterTAG) with stop codon mutagenesis
                Add seqPos to betterTAA
            Else
                Add seqPos to TAAmatches
        If codon == TAC or TAT
            # Simplified - other factors play into the role of the +6nt
            If sequence + 6 == T or C
                # Y is the symbol for C or T
                Add seqPos to betterTAY
            Else
                Add seqPos to TAYmatches
    Else go back to start

## Compare ##
If the length of CAGmatches == 0
    If the length of CAAmatches == 0
        Print you're SOL
    Else
        If the length of betterTAG == 0
            If the length of TAGmatches == 0
                print CAAmatches, say to look in more detail
            Else
                Iterate through TAGmatches
                    Iterate through CAAmatches
                        If TAGelement == (CAAelement - 3)
                            Add to bestOptions
                        If TAGelement == (CAAelement + 3)
                            Add to okayOptions
                        Else
                            Keep going through CAAmatches
                    # go to the next TAGelement
        Else
            Iterate through betterTAG
                Iterate through CAAmatches
                    If TAGelement == (CAAelement - 3)
                        Add to bestOptions
                    If TAGelement == (CAAelement + 3)
                        Add to okayOptions
                    Else
                        Keep going through CAAmatches
                # go to the next TAGelement
Else
    If the length of betterTAG == 0
        If the length of TAGmatches == 0
            print CAGmatches, say to look in more detail
        Else
            Iterate through TAGmatches
                Iterate through CAGmatches
                    If TAGelement == (CAGelement - 3)
                        Add to bestOptions
                    If TAGelement == (CAGelement + 3)
                        Add to okayOptions
                    Else
                        Keep going through CAGmatches
                # go to the next TAGelement
    Else
        Iterate through betterTAG
            Iterate through CAGmatches
                If TAGelement == (CAGelement - 3)
                    Add to bestOptions
                If TAGelement == (CAGelement + 3)
                    Add to okayOptions
                Else
                    Keep going through CAGmatches
            # go to the next TAGelement
"""