'''
Created on Jul 5, 2019

@author: underit

'''
n = input('Unesite broj:')
total = 0
for i in range(1,int(n)):
    total+=i
print('Zbir prvih ' + n + ' je :' + str(total))