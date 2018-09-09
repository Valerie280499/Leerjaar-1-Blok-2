#gebruik dit programma om uit te breiden naar een programma
#dat zowerl DNA als eiwit accepteert.


def main():
    soort = input('Wat voor sequentie wilt u invoeren? (dna/eiwit)')
    seq = infvoer() 
    print("Dit is uw sequentie:", seq)


def invoer(soort):
    sequentie =  input("Voer uw",soort.'sequentie in:')
    
    if soort DNA:
        isdna = check_dna(sequentie)
        if isdna == False:
            raise TypeError
        
    elif soort eiwit:
        isaa = check_eiwit(sequentie)
        if isaa == False:
            raise TypeError
        
    return sequentie

def check_aa(seq):
    seq = seq.upper()
    for aa in seq:
        if aa in ['B','J','O','U','X','Z']
        return False
    return True

