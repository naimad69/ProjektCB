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

print(plk)






