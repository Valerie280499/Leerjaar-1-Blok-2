#les 4 blok 2

Text mining
-Text mining is het zoeken van patronen in of tussen tekstbestanden
om hier nieuwe informatie uit te halen.

http://www.diveintopython.net/

#strings
-slicen
-converteren

str.find(substr)
str.replace(old,new)
str.split(delim)
str.join(str) #plakken van strings
str.strip() #verwijderen van o.a. spaties

str.rstrip()
str.upper()
str.isupper() #toetsen of een string uit hoofdletters bestaant
str.isdigit() #toetsen of iets uit cijfers bestaat

'hello world'.find('o')

Regular expressions
-Geven je de mogeljkheid om te zoeken op complexere teskst patronen.
-Binnen de bio-informatica zijn we veel op zoek naar complexe tekst patronen.

-Denk maar aan:
    -Stopcodons
    -
    -

'hallo' en 'hello' --> h[ea]llo
-Heeft zijn eigen syntax en betekenis van symblolen
-Linux systemen maken veel gebuik van regex,
-
-


syntax:
. (punt)        precies een willekeurig teken               h.llo
* (asterisk)    0, 1 of meer van het voorgaande teken       h*llo   llo
+ (plus)        1 of meer van het voorgaande teken          h+llo   hllo, hhhhllo
? (vraagteken)  exact 0 of 1 van het voorgaande teken       h?llo   llo, hllo
^ (dakje)       geeft aan dat het er mee moet beginnen      
$ (dollar)      geeft aan dat het er mee moet eindigen
( | )           een 'of' keuze

[] aantal tekenis waaruit gekozen kan worden, '^' betekent de inverse
() een groep
\  Escape character
{m,n} minimaal m en maximaal n van het voorgaande teken

\?
\\ --> \\+

#voorbeeldje:
'bla'
'blaaaa'
'blaa'

bla{1,4}

#voorbeeldje 2:
We willen graag een match vinden op 'Hello World' en op 'Hallo Wereld',
omdat we iet weten in welke taal de tekst geschreven is.

overeenkomsten: H'[ea]'llo  W[oe]r 'e?' ld

#voorbeeld 3:
1234 AB--> [1-9]{4}/s?[A-Z]{2}


import re    De import die je nodig hebt om te werken met regex

re.search    Zoeken naar overeenkomsten
    -re.search(pattern, string, flags=0)
        - Pattern, is het zoeken naar een patroon/
        - String is de teskt waarin je het patroon wilt vinden
        - Flags heeft een default 0, geef je meestal dus niet mee.
          Hiermee kun je opties meegeven.
        
    matchObject = re.search(r'.*ATG.*', line)
    print(matchObject)
    
re.sub
    -re.sub(pattern, repl, string, max=0)
        - Zoek naar pattern
        - Vervang pattern met repl
        - Zoek in string
        - Max is maximum aantal keer dat de substitutie gedaan wordt,
          0 is default en zorgt voor vervanging van alles. 
    
re.split
    -re.split(pattern, string,maxsplit=0,flags=0)
        - Zoek op pattern in tsring
        - Split string op basis van pattern
        - Lever een lijst op als resultaat
        - Maxsplit is het aantal keer dat de splitsing plaatsvind,
          indien 0 dan alle voorkokmen van pattern. 

re.compile als je een patroon meerdere malen wilt gebruiken in je code is het handig om deze te comileren
        - prog = re.compile(pattern)
        - result = prog.match(string)
            is gelijkj aan:
            result = re.match(pattern, string)

        -maar het patroon wordt efficienteer opgeslagen dan wanneer je
         steeds een string moet compilteren.

#matchobject eigenschappen
- matchObj.group()  - retourneert een of meerdere subgroepen van de match,
                      default 0, ofwel alle groepen
- matchObj.start()  - retourneert de stratpositie an de match
- matchObj.end()    - retourneert de eindpositie van dematch
- matchObj.span()   - retourneert een tuple met start en eind positie

#oefening 1:
import re

seq = input('DNA sequentie:')
start_codon = 'ATG'
stop_codons = [[],[],[]]

for line in seq:
    match_start = re.search(start_codon,seq)
    match_stop = re.search('TAA|TAG|TGA',seq)
print(match_start)
#print(match_stop)

print('start',match_start.start())
print('eind',match_start.end())
pattern = '([ATGC]{3})'
#print(re.split(pattern,seq))


#(sub)groepen
(sub)groepen geef je aan met ronde haken.
m.group(0)      --> 'isaac newton'
m.group(1,2)    --> ('isaac','newton')

