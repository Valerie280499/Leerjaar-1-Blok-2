
doorgaan = 'true'
counter = 0

try:
    while doorgaan is 'true':
        counter += 1
        print(counter)
        doorgaan = 'true'
except KeyboardInterrupt:
    print('\n Sorry keyboard was interrupted')
'''
'''
def main():
    try:
        items = invoer()
        print('Dit zijn de items', items)

    except IndexError:
        print('Te weinig items of te veel')

def invoer():
    lijstje = input("Voer 5 items in:")
    new = lijstje.split(",")

    if len(new) != 5:
        raise IndexError
    return new

main()
'''
'''
def main():
    try:
        fil = openFile("bestand")
    except FileNotFoundError as fnfe:
        print(fnfe.args[0])
def openFile(naam):
    if naam == "bestand":
        raise FileNotFoundError("Bestand mist")
    fil = open(naam)
main()
'''
