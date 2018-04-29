plik=open('C:\\Users\\Uczeń\\Downloads\\wyniki-lotto-sortowane.csv', 'r+')


plk=plik.readlines()
plk.pop(0)

lng=len(plk)

x=0

while x<lng:
    plk[x]=plk[x].replace('\n', '')
    x=x+1

for i in range(lng):
    plk[i]=plk[i].split(';')

i=0


dic={}

for x in plk:
    dic[x[0]]={'numer':x[0], 'dzien':x[1], 'miesiac':x[2], 'rok':x[3], 'liczby':x[4:]}


print(dic)

print(dic[x[7]])






