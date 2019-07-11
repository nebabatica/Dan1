'''
Created on Jul 5, 2019

@author: underit
'''


def napraviAkronim(punNaziv):
    ispis = ""
    for i in punNaziv:
        if i.isupper() == True:
            ispis += i
            
    return ispis


unos = input('Unesite pun naziv : ')
print(napraviAkronim(unos))
