# les 2 blok2
# Matplotlib
# Valerie Verhalle
# Klas: BIN-1e
# Datum: 22-11-2017

'''
staaf-lijn diagrammen; boxplot; topografisch; 
Scatterplot
Lijndiagram
Staafdiagram
Taartdiagram
Boxplot

Vaak nodig:
- Import matplotlib.pyplot as plt
- From random import randint
- Range()

Data:
- X data
- Y data
- (behalve een taartdiagram)

X en Y data matchen op basis van index
- Dus moeten ze even lang zijn!
'''
#uitleg diagrammen

import matplotlib.pyplot as plt
import numpy as np

#staafdiagram
barx = [1,2,3,4]
bary = [10,20,10,15]
plt.bar(barx,bary)
plt.show()

#lijndiagram
linex = [1,2,3,4]
liney = [10,20,10,15]
plt.plot(linex,liney)
plt.show()

#scatterplot
scatx = []
scaty = []
from random import randint
for i in range(0,100):
    scatx.append(randint(10,20))
    scaty.append(randint(0,50))
plt.scatter(scatx,scaty)
plt.show()

#taartdiaram
labels = ['Studenten', 'Docenten','Secretariaat', 'Overig']
percentages = [45, 30, 20, 5]
plt.pie(percentages, labels=labels, autopct='%1.1f%%')
plt.title("Percentage beroep ondervraagden")
plt.show()

#plaatjes
form scipy import ndimage
from scipy import misc
kitten = ndimage.emread('kitten.jpg')
kitten_new = ndimage

'''
Subplots:
Er zijn meereremanieren waarop je een plaatje met meerdere
dataseets kunt maken.
- Meerdere lijnen in een grafiek
- Meerdere grafieken in een plaatje
'''

#Subplots: meerdere grafieken:
fig, axs = plt.subplots(nrows=2, ncols=1)
axs[0] = plt.plot(x_test,y_test)
axs[1] = plt.plot(x_placebo,y_placebo)
fig.show() #of plt.show()

#Subplots: meerdere lijnen
import matplotlib.pyplot as plt
x_data =
y_data =
x-data =
y_data=

plt.plot(x_data,y_data, color ='blue')
plt.plot(x_data,y_data, color ='red')

#Begrippen:
nrows: Bebaald aantal rijden in fig
ncols: Bepaald aantal kolommen in fig
pwp!

'''
Input niet alleen lists!
-np.array()
    pwp!
'''
'''
Grafiek eigenschappen:
Titel:              plt.title()
Legenda:            plt.legend()
x-as omschrijving:  plt.xlabel()
y-as omschrijving:  plt.ylabel()
'''

#oefening 1
import matplotlib.pyplot as plt
import numpy as np

barx =[1,2,3,4,5,6,7,8,9,10]
bary = []
from random import randint 
for i in range(len(barx)):
    bary.append(randint(10,21))
x_np = np.array(barx)
y_np = np.array(bary)

plt.bar(barx,bary)
plt.show()


#oefening 2
import matplotlib.pyplot as plt
import numpy as np

x_data = [1,2,3,4,5,6,7,8,9,10]
y_data = []

from random import randint
for i in range(len(x_data)):
    y_data.append(randint(10,21))
x_np= np.array(x_data)
y_np= np.array(y_data)

plt.plot(x_data,y_data)
plt.show()


#oefening 3
import matplotlib.pyplot as plt
import numpy as np

x_data = [1,2,3,4,5,6,7,8,9,10]
y_data = []
y_data2 = []

from random import randint
for i in range(len(x_data)):
    y_data.append(randint(10,21)) #y1_data =[randint(10,20) for i in range(0,10)]
    y_data2.append(randint(10,21)) #y2_data =[randint(10,20) for i in range(len(x_data)))
    
plt.plot(x_data,y_data,color='blue',label='blauwe lijn')
plt.plot(x_data,y_data2,color='red', label='rode lijn')
plt.show()
