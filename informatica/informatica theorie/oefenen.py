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
