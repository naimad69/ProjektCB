int=[4,2,9,7,1]
float=[1.1,2.2,3.3,4.4,5.5]
str=['arka','gdynia','kurna','świnia']
miesz=[123,'xyz',3.14]

print(int[0:5])
print(float[0:5])
print(str[0:5])
print(miesz[0:5])

print('\n')

int.extend([9,9,9])
print(int[0:8])

float.extend([9,9,9])
print(float[0:8])

str.extend(['qwe','rty','uio'])
print(str[0:8])

miesz.extend([9,9,9])
print(miesz[0:8])

print('\n')

int.sort()
print(int[0:8])

float.sort()
print(float[0:8])

str.sort()
print(str[0:8])

print('\n')

int.reverse()
print(int[0:8])

float.reverse()
print(float[0:8])

str.reverse()
print(str[0:8])

miesz.reverse()
print(miesz[0:8])

print('\n')

int.pop(3)
print(int)

float.pop(3)
print(float)

str.pop(3)
print(str)

miesz.pop(3)
print(miesz)