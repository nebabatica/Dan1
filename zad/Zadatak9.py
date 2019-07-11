'''
Created on Jul 5, 2019

@author: underit
'''


def izracunajKaznu(brzinaVozila, ogranicenje):
    if brzinaVozila <= ogranicenje:
        print('Sve je uredu.')
    else:
        ukupnaKazna = 0
        dinZaSvakiKm = (brzinaVozila - ogranicenje) * 500
        ukupnaKazna = 5000 + dinZaSvakiKm
        if brzinaVozila > 120:
            brzinaVozila += 10000
        print('Ukupna kazna iznosi :' + str(ukupnaKazna) + " din")
            
        
izracunajKaznu(120, 100)