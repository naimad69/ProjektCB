import random
import time


lista=['kamień','papier','nożyce']

random.seed(time.time())
x = random.randint(0,2)



wybor=input('Co wybierasz?: ')

while wybor!='koniec':

        if lista[x]=='kamień' and wybor=='papier':
            print('Wygrałeś')
        elif lista[x]=='kamień' and wybor=='nożyce':
            print('Przegrałeś')
        elif lista[x]=='kamień' and wybor=='kamień':
            print('remis')
        elif lista[x]=='papier' and wybor=='papier':
            print('Remis')
        elif lista[x]=='papier' and wybor=='nożyce':
            print('Wygrałeś')
        elif lista[x]=='papier' and wybor=='kamień':
            print('Przegrałeś')
        elif lista[x]=='nożyce' and wybor=='papier':
            print('Przegrałeś')
        elif lista[x]=='nożyce' and wybor=='nożyce':
            print('Remis')
        elif lista[x]=='nożyce' and wybor=='kamień':
            print('Wygrałeś')
        else:
            print('Wpisz kamień, papier, lub nożyce')
        x = random.randint(0, 2)
        wybor = input('Co wybierasz?: ')


