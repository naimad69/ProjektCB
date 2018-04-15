import random
import time

T=0
K=0


lista=['kamień','papier','nożyce']

random.seed(time.time())
x = random.randint(0,2)



wybor=input('Co wybierasz?: ')

while wybor!='koniec':

        if lista[x]=='kamień' and wybor=='papier':
            print('Wygrałeś')
            T=T+1
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='kamień' and wybor=='nożyce':
            print('Przegrałeś')
            K=K+1
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='kamień' and wybor=='kamień':
            print('remis')
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='papier' and wybor=='papier':
            print('Remis')
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='papier' and wybor=='nożyce':
            print('Wygrałeś')
            T = T + 1
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='papier' and wybor=='kamień':
            print('Przegrałeś')
            K = K + 1
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='nożyce' and wybor=='papier':
            print('Przegrałeś')
            K = K + 1
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='nożyce' and wybor=='nożyce':
            print('Remis')
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        elif lista[x]=='nożyce' and wybor=='kamień':
            print('Wygrałeś')
            T = T + 1
            print('Twoje punkty', T)
            print('Punkty przeciwnika', K)
        else:
            print('Wpisz kamień, papier, lub nożyce')
        x = random.randint(0, 2)
        print('\n')
        wybor = input('Co wybierasz?: ')



