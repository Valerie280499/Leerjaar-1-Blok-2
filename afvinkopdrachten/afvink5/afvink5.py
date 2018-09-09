#Valerie Verhalle
#afvink5
import re
def main():
    bestand = 'Felis.fa'
    seqs = deel2(bestand)
    percentage(seqs)
        
def percentage(seqs):
    perc_list = []
    for index in seqs:
        #print(index)
        G = 0
        C = 0
        for letter in index:
            if letter is 'G':
                G+=1
            elif letter is 'C':
                C+=1

        #print('G:',G,'C:',C,'GC%:')
        perc = ((G+C)/len(index))*100
        perc_list.append(perc)
    print(max(perc_list))

def deel2(bestand):
    bestand = open(bestand)
    headers = []
    seqs = []
    seq = ''

    for line in bestand:
        line = line.strip()
                
        if ">" in line:
            headers.append(line)
            if len(seq) > 0:
                seqs.append(seq)
                seq = ''
        else:
            seq += line
    seqs.append(seq)

    return seqs




main()
class DNA:
    def __init__(self,seq):
        self.setDNA(seq)
        
    def setDNA(self,seq):
        self.DNA = seq

        lengte = len(self.DNA)
        count = 0
        nuc = 'T|C|G|A|N'


        for i in self.DNA:
            match = re.search('[^TCGAN]',self.DNA)
            if match != None:
                count += 1
        
        if count == lengte:
            print('je hebt onzuiver DNA')
        else:
            print('je hebt zuiver DNA!')
            
  
    def getDNA(self):
        return self.DNA

    #zet 'T' om in 'U' maar zet deze niet goed terug in self.DNA
    def getTranscript(self):
        trans = self.DNA
        trans = trans.replace('T','U')
        return trans
    
    def getLength(self):
        return len(self.DNA)

