'''
Created on Jul 5, 2019

@author: underit
'''


def izracunajOcenu(brojBodova):
    if brojBodova < 50:
        return 5
    elif 50 <= brojBodova < 60:
        return 6
    elif  60 <= brojBodova < 70:
        return 7
    elif 70 <= brojBodova < 80:
        return 8
    elif 80 <= brojBodova < 90:
        return 9
    elif 90 <= brojBodova <= 100:
        return 10
    else:
        print('Niste dobro uneli broj bodova')
        
print(str(izracunajOcenu(101)))