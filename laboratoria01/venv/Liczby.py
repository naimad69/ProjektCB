plik=open('C:\\Users\\Uczeń\\Downloads\\wyniki-lotto-sortowane.csv', 'r+')


plk=plik.readlines()
plk.pop(0)

for i in plk:
    plk.replace('\\n', '')

print(plk)






