#les 1 blko2 
'''
Debugging is het zoeken naar fouten in een programma dat wordt ontwikkeld.
Deze fouten zijn bekend.

Testen is het zoeken naar onbekende fouten. Verondersteld wodt dat
het programma juist werkt.


'''
'''
Compile error
-Treedt op tijdens compileren
-Programma kan niet runnen
-De compile error wordt verholpen door de programmeur 
-Is altijd ongewenst

Exception
-Treedt op tijdens uitvoer
-Programma kan runnen totdat de exception op zal treden.
-De exception zal niet altijd optreden
-Is soms gewenst


-Bij de uitvoer van een programma kunnen er fouten optreden
-Deze fouten die je verwacht kun je afvangen in een exception
handling

Documentatie exceptions:
https://docs.python.org/3/library/exceptions.html

Deling door nul: ZeroDivisionError
estand openen dat niet bestaat: IOError

Zelf errors opgooien
Kan met raise
	Sytax:
		raise <eenofandereerror>

Vaak in combinatie met een if else structuur
	if <conditie van toepassing>:
		raise <error>

Samenvatting:
Python kent een groot aantal ingebouwde exceptions
Deze kan je afvangen met een try/except structuur

Compile errors ontstaan door fouten in de code/syntax
Deze moet je oplossen om het programma te laten werken debuggen)

Exceptions ontstaan door onverwachte problemen tijdens het draaien van het programma
Deze kan je oplossen door plannen en testen
'''
