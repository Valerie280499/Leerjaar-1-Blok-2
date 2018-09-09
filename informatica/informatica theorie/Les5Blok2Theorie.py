#Object orientatie
- Is een andere manier van promgrameren
- Het idee erachter is om de realiteit te benaderen.
    - Met object orientatie creeer je
    objecten die afgeleid zijn van de werklijke objecten.
    
#Procedureel
- Data en functies liggen los van elkaar
- Functies dragen waardes over

#Object orientatie
- Data en functies horen bij elkaar
- Objecten roepen elkaar aan.

de drie kenmerken van object orientatie:
- Encapsulatie
-inheritance
-poly

#encapculatie
setter: stelt variabele in
gettter: vraag variabele op

- Je kan van buitenaf geen invloed meer uitoefenen op de variabelen
- Omgeven van data(variabelen) met functionaliteit (functies)
- De variabeen zijn alleen te veranderen via de functies.
- Encapsulatie voorkomt dat data benaderbaar is
- Hierdoor worden 'onmogelijke' waardes voorkomen.

#classes
- Een class is als een blauwdruk voor een huis.
- Een blauwdruk kan vele malen gebruit worden
    om steeds hetzelfde huis te bouwen.

#voorbeeld 1:
class auto:
    def setSnelheid(self,v):
        self.snelheid =v
    def getSnelheid(self):
        return self.snelheid
    def setSnelheid(slef,v):
        if v>0 and v<200:
            self.snelheid = v
        else:
            print('Onmogelijk')


'''
>>> a = auto()
>>> a.setSnelheid(20)
>>> a.getSnelheid()
>>> 20
>>> a.setSnelheid(500)
>>> Onmogenlijk
'''


#instanties
- classes hebben elk dezelfde blauwdruk maar ze zijn toch anders door andere
    variabelen.

#instances and constructors
een begin waarde meegeven voor een bepaalde variabelen

def_init_(self,v):
    self.setSnelheid()

er moet nu een beginwaarde worden ingevult op het moment dat je een nieuwe
variabele aanvraagt. 

#
UML i.p.v. flowcharts

#inheritance
- Een electrische auto kan overerven van auto,
heeft alle kenmerken van eenauto met nog estra eigenschappen. 
- superclass en subclass.

    class Sequentie:

    class DNA(Sequentie):

#polymorifse
- Letterlijk veelvormig gedrag
- Iedere auto kan rijden, maar hoe die auto gaat
    rijden is afhankelijk van het type.


#voorbeeldje 2:
class boom:
    def __init__(self, h, b):
        self.setHoogte(h)
        self.setBlad(b)
        
    def setHoogte(self, h):
        self.hoogte = h
    def getHoogte(self):
        return self.hoogte
    
    def setBlad(self,b):
        self.blad = b
    def getBlad(self):
        return self.blad

class kerstboom(boom):
    def __init__(self, h, b, D):
        self.setHoogte(h)
        self.setBlad(b)
        self.setDecoratie(D)
        #boom.__init___(self,'Naald',h)
        
    def setDecoratie(self, D):
        self.decoratie = D
    def getDecoratie(self):
        return self.decoratie


#voorbeeldje 3:
class dier:
    def __init__(self,voortbeweging, aantalpootjes):
        self.setBewegen(voortbeweging)
        self.setPootjes(aantalpootjes)
        
    def setBewegen(self, voortbeweging):
        self.__bewegen = voortbeweging
        
    def getBewegen(self):
        return self.__bewegen

    def setPootjes(self,aantalpootjes):
        self.__aantal_pootjes = aantalpootjes

    def getPootjes(self):
        return self.__aantal_pootjes
    

#koe = dier()
#koe.setBewegen('loopt')

class zoogdier(dier):
    def __init__ (self):
        self.setBewegen('loopt')
        self.setPootjes(4)
        
    def maak_geluid(self):
        return "Maakt een zoogdiergeluid"

class alpaca(zoogdier):
    def spuugt(self):
        return 'Alpaca spuugt'
    def maak_geluid(self):
        return 'Maakt een alpaca geluid'

def main():
    harry = alpaca()
    print(harry.getPootjes())
    print(harry.getBewegen())
    print(harry.spuugt())
    print(harry.maak_geluid())

main()


