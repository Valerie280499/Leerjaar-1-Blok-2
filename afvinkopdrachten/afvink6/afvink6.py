import time
import re

def main():
    T = time.clock()
    for i in range(1,20):
        fi = fib(i)
        print(fi)
    print('recursieve fucntie:', T)

    C = time.clock()
    for i in range(0,19):
        inter = fibit(i)
        print(inter)
    print('iteratieve functie:',C)
    
    bestand = open('sequence.fasta')
    seq = 'ATGACA'
    print(controle(seq))
    
#recursieve functie reeks van Fibonacci
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
#iteratieve functie reeks van Fibonacci
def fibit(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a


def controle(seq):
    if len(seq) != 0:
        if re.match('A|T|G|C', seq[0]):
            return controle(seq[1:])
        else:
            return 'Je hebt onzuiver DNA!'
    else:
        return 'Je hebt zuiver DNA!'

main()



