import sys
import re

def concatBase(string):
    if(len(string)==1):
        return string
    else:
        return "["+string+"]"

def iupacToBase(iupac):
    transform={"A":"A","C":"C", "G":"G",
           "T":"T", "R":("A", "G"),
           "Y":("C", "T"),
           "S":("C", "G"),"W":("A", "T"),
           "K":("G", "T"), "M":("A", 
            "C"), "B":("C", "G", "T"),
           "D":("A", "G", "T"), "H":("A", "C", "T"),
           "V":("A", "C", "G"), "N":["A", "C", "G", "T"]}
    return "".join([concatBase("".join(transform[i])) for i in iupac])
    
def applyRegx(string,dnaseq):
    ## Find the flag to ignore case
    return [i.start() for i in re.finditer(iupacToBase(string),dnaseq)]

def within(start,end,motiflocs):
    return [i-start for i in motiflocs if i>= start and i< end]
    

def findMotifLocs(motif,dnaseq,newlines):    
    motiflocs=applyRegx(motif,dnaseq)
    motifPerString=[within(i,j,motiflocs) for i,j in zip(newlines[0:len(newlines)-1], newlines[1:len(newlines)])]
    return motifPerString

def main(dnaseq,motifs):
    dnafile=open(dnaseq)
    dnaseq=dnafile.read()
    newlines=[i.start() for i in re.finditer("\n",dnaseq)]
    found=[] # could initialize
    count=[]
    which=[]
    ## add better names than t1 t2 and t3
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
        dnaseq=sys.argv[1]
        print dnaseq
    else:
        dnaseq="/Users/agriffith/Dropbox/clean.csv"
    ## Current Readthrough values by stop codons
    motifs=[("CAGCTA",1),("GGGCAA",2),("TTGCCC",2),("CAAGAA",2)]
    main(dnaseq,motifs)
