#les 6 blok 2
#hoofdstuk 12 in boek


#Recursie:
- Droste effect is ook bekend als visuele recursie.
- Patroon in een patroon in een patroon.....
- Recursie is een fuctie die zichzelf aanroept.
- Het is de tegenhanger van iteratie (forloops)
    - voordelen: elegant; expressief.
    - nadelen: performance; overhead.

    percoramce hangt af van de programmeertaal

#faculteit:
3 facultiet = 3! = 3*2*1
              n! = n*(n-1)
#voorbeeld 1
def main():
    getal = int(input('nummer'))
    print(faculteit(getal))

def faculteit(num): #4*3*2*1
    if num == 0:
        return
    else:
        return num * faculteit(num-1)
main()

fac(4)
fac(4*fac(3))
fac(4*3*fac(2))
fac(4*3*2*fac(1))
fac(4*3*2*1*fac(0))
fac(4*3*2*1*1)


# Fibonacci number
- Fn = F(n-1) + F(n-2),

#voorbeeld 2:
def main():
    for i in range(1:11):
        fib(i)

def Fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


#voorbeeld 3:
def main():
    print(isAlfa('woord'))

def isAlfa(woord):
    if len(woord) == 0:
        return True
    else:
        if re.match('[a-zA-z]',woord[0]):
            return isAlfa(woord[1:])
        else:
            return False
main()


main()
