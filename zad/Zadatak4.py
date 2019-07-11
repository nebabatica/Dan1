'''
Created on Jul 5, 2019

@author: underit
'''
brojBrojeva = int(input('Unesite broj brojeva :'))
zbir = 0
while brojBrojeva > 0:
    temp = int(input('Unesite broj '))
    zbir += temp
    brojBrojeva-=1
print('Zbir svih unetih brojeva je  :' + str(zbir))
