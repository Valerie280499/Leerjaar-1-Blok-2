#les3Blok2Theorie
'''Niet elke data is het zelfde, dus leren we verschillende datastructuren

Datastructuren:
-String
-List
-Tuples
-Float
-Integer

-Versnellen bepaalde processen
-Inzichtelijk
-Intuitief

#tree
#graph
#lijsten
-makkelijk om lineaire data op te slaan
-Binnen informatica noemen we dit meestal een array

-Geordend
-Duurt lang om 1 item te zoeken in een lijst.

#dictionary
-In de inforamtica noemen we deze structuur ook wel hashmaps
-Hashmaps maken het moglijk heel snel een waarde terug
 te vinden, door key-value paren te maken.
-Het opvragen van wat er in een dictioinary zit kan met keys() en values()

-Zijn ongeschikt om van value naar key te zoeken!!!
-Bevat altijd een sleutel-waarde combinatie

'''

#opdracht 1
animal_dict = { "zoogdieren" :['dolfijnen','alpaca','koe'],
                "insecten" :['mier','bladluis','bij'],
                "birdys" :['papegaai','mus','uil']}
print(animal_dict.keys())
print(animal_dict.values())
print(animal_dict['zoogdieren'])

teller = 0
lijst = list(animal_dict.values())
for dieren in lijst:
    if 'papegaai' in dieren:
        print('Een papgegaai behoort tot de',list(animal_dict.keys())[teller])
    teller +=1

#opdracht 2
#toevoegen van een niewe key en values:
animal_dict["vissen"] = ['zebravis','gup','clownsvis']
print(animal_dict)

#verwijder een bepaalde value:
animal_dict['zoogdieren'].remove('dolfijn')

#voeg dolfijn toe aan vissen
animal_dict['vissen'].append('dolfijn')

'''
#sets
-Komen van het wiskunde concept'verzamelining'
-Sets hebben een aantal belangrijke eigenschappen
    -Ze bestaan uit unieke waardes
    -Ze hebben geen indexen
    -Ze zijn ongeordend
    -Ze kennen hun eigen methodes, zoals
        • Bepalen wat het verschil is tussen twee sets,
        • Ewee sets samenvoegen
        • Etc...
    – Ze zijn mutable (net als lists)

Set wil graag iets waar hij over kan itereren. Dit mag dus
vanalles zijn, maar veel gebruikt is een lijst of een tuple.
nieuwe_set = set(<iterable>)

Add wil graag een element toevoegen aan de set. Dit kan het
een en ander zijn, zoals strings, ints, tuples, maar geen lijsten
of andere sets.
nieuwe_set.add(<element>)
'''

boerderij = set(["lama","koe","kip","varken","lama"])
dierentuin = set(["lama","giraffe","leeuw","flamingo","olifant"])
#print(boerderij)
#print(dierentuin)

#Je kan een set dus niet gebruiken om te tellen hoe vaak een waarde
#voorkomt, maar wel wat de unieke waardes zijn.

#Set methoden:
set1.add(elem)          Toevoegen van element
set1.union(set2)        Samenvoegen van twee sets
set1.intersection(set2) Overlap tussen twee sets
set1.difference(set2)   Verschil tussen set1 en set2, vanuit set1 gezien
set1.issubset(set2)     Is elk element uit set1 onderdeel van set2
set1.issuperset(set2)   Is elk element uit set2 te vinden in set1
set1.remove(elem)       Verwijderen van element uit set

boerderij = set(["lama","koe","kip","varken","lama"])
dierentuin = set(["lama","giraffe","leeuw","flamingo","olifant"])

#Union
beesteboel = boerderij.union(dierentuin)
print(beesteboel)       --> {'olifant', 'koe', 'kip', 'leeuw', 'giraffe', 'varken','flamingo', 'lama'}

#Intersection
beesteboel = boerderij.intersection(dierentuin)
print(beesteboel)       --> {'lama'}

#Difference
beesteboel = boerderij.difference(dierentuin)
print(beesteboel)       --> {'koe', 'varken', 'kip'}

#Symmetric Difference
beesteboel = boerderij.symmetric_difference(dierentuin)
print(beesteboel)       --> {'flamingo', 'giraffe', 'olifant', 'varken', 'koe', 'kip','leeuw'}

#Issubset / issuperset
vee = set(["koe","kip","varken"])
print(vee.issubset(boerderij))      --> True # zoals te verwachten, elk dier in vee zit in boerderij
print(vee.issubset(dierentuin))     --> False # maar niet in dierentuin
print(boerderij.issuperset(vee))    --> True # dat maakt ook dat boerderij superset is van vee

#Remove
boerderij.remove("lama")
print(boerderij)        --> {'varken', 'kip', 'koe'}

#opdracht 3
planeten = set(['Mercurius','Venus','Aarde','Mars','Jupiter','Saturnus','Uranus','Neptunus','Pluto'])
hemellichamen = set(['Aarde','Zon','Pluto'])

planeten.symmetric_difference(hemellichamen)
planeten.intersection(hemellichamen)
zonnestelsel = planeten.union(hemellichamen)
print(zonnestelsel)

print(zonnestelse.issuperset(planteten))
print(zonnestelsel.issuperste(hemellichamen))
planeten.remove('pluto')
print(planeten)











