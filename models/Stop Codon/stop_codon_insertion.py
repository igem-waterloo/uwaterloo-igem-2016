import sys
import re

"""
This programme is intended to be used to control expression of constructs in
yeast cells that are in a [PSI+] prion state.

Input: in-frame nt sequence of genetic construct
Output: the top-scoring bp positions with respect to predicted readthrough
    efficiency during a [PSI+] response
"""

# Concatenates the provided bases
def concatBase(string):
    if(len(string)==1):
        return string
    else:
        return "["+string+"]"

# Enables processing of sequences with ambiguous nt reads
def iupacToBase(iupac):
    transform={
        "A":"A",
        "C":"C",
        "G":"G",
        "T":"T",
        "R":"AG",
        "Y":"CT",
        "S":"CG",
        "W":"AT",
        "K":"GT",
        "M":"AC",
        "B":"CGT",
        "D":"AGT",
        "H":"ACT",
        "V":"ACG",
        "N":"ACGT"}
    return "".join([concatBase(transform[i]) for i in iupac])

# Custom definition of Regx searching
def applyRegx(string,dnaseq):
    ## Find the flag to ignore case
    return [i.start() for i in re.finditer(iupacToBase(string),dnaseq)]

# Check if the motif if present between start and end
def within(start,end,motiflocs):
    return [i-start for i in motiflocs if i>= start and i< end]

# Returns the locations in the sequence
def findMotifLocs(motif,dnaseq,newlines):
    motiflocs=applyRegx(motif,dnaseq) #finds locations
    starts = newlines[:-1]
    ends = newlines[1:]
    motifPerString = [within(i,j,motiflocs) for i,j in zip(starts, ends)]
    return motifPerString

def main(dnafile,motifs):
    with open(dnafile, 'r') as f:
        dnaseq = f.read()
    newlines=[i.start() for i in re.finditer("\n",dnaseq)]
    found=[] # could initialize
    count=[]
    which=[]
    ##
    for mot in motifs:
        t1=findMotifLocs(mot[0],dnaseq,newlines)
        found.append(t1)
        t2=sum([len(i) for i in t1])
        count.append(t2)
        t3=[(n,i) for i,n in zip(t1,range(len(t1))) if len(i)>0]
        which.append(t3)

    foundMotifs=[(mot,loc) for mot,count,loc in zip(motifs,count,which) if count>0]
    for i in foundMotifs:
        print i


if __name__ == '__main__':
    if len(sys.argv) > 1:
        dnafile=sys.argv[1]
        print dnafile
    else:
        dnafile="clean.csv"
    ## Current Readthrough values by stop codons
    motifs=[("CAGCTA",1),("GGGCAA",2),("TTGCCC",2),("CAAGAA",2)]
    main(dnafile,motifs)
