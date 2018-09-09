import re
import pickle

def main():
    bestand = 'file1.fa'
    headers, seqs = lees_inhoud(bestand)
    p53_patroon(seqs,headers)
    p53_eiwit()
    
    fasta = open('sequence.fasta').readlines()[1:]
    fasta_file = ''
    for line in fasta:
        fasta_file += line.strip()
    puur_DNA(fasta_file)

    fasta = open('sequenceColi.fasta').readlines()[1:]
    Coli_fasta = ''
   
    for line in fasta:
        Coli_fasta += line.strip(',')
        Coli_fasta += '\n'
    
    coli_DNA(Coli_fasta)
    

def lees_inhoud(bestand):
    bestand = open(bestand)
    headers = []
    seqs = []
    seq = ""

    for line in bestand:
        line = line.strip()
                
        if ">" in line:
            headers.append(line)
            if len(seq) > 0:
                seqs.append(seq)
                seq =""
        else:
            seq += line
    seqs.append(seq)

    return headers, seqs

def p53_patroon(seq,headers):
    print(80*'-')
    count = 0
    print('Headers van de sequenties waar het p53 eiwit in voorkomt:')
    
    for index in range(len(seq)):
        search = re.search("MCNSSC[MV]GGMNRR",seq[index])
        
        if search != None:
            count += 1
            print(headers[index],'\n')
            
    print('Het p53 eiwit komt in', count,'sequenties voor.')
            
def p53_eiwit():
    print(80*'-')
    with open('aa3.pickle', 'rb') as f:
        aa3 = pickle.load(f)

    eiwitten = aa3.keys()
    seq = "MCNSSC[MV]GGMNRR"

    for i in range(1):
        for index in seq:
            eiwit = index
            
            for index in eiwitten:
                if index[0] == eiwit:
                    print(eiwit,'match',index)
                    
            if index[0] != eiwit:
                print(eiwit)
    print(seq)

def puur_DNA(fasta):
    print(80*'-')
    fout = 0
    
    for index in fasta:
        search = re.search("[ATGC].*", index)
        
        if search is None:
            fout += 1
            print('Foute letter',index,'Op positie:', test.index(index),'Searchtype:', search)

    if fout == 0:
        print('Je sequentie is puur DNA!')

def coli_DNA(fasta):
    print(80*'-')
    match = 0
    count_1 = 0
    count = 0
    
    for index in fasta:
        count_1 += 1
    total = int(count_1/7)
    
    print('Totaal aan stikstofbase:',count_1,'gedeeld door 7:', total)
    print('Indexen van de consensuspatronen:')
    
    for index in range(total):
        search = re.search("AGGAGGT", fasta[count:count+7])
        count += 1
        
        if search != None:
            match += 1
            
            print(fasta.index(fasta[count:count+7]))
    print('Het consensuspatroon van de promoter van E.coli komt', match,'keer voor.')

main()

