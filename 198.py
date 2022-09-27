a = int(input())
b = int(input())
c = int(input())

if (a**2 + b**2) < c**2:
    print('Obtuse')
elif (a**2 + b**2) > c**2:
    print('Acute')
elif (a**2 + b**2) == c**2:
    print('Rectungular')
else:
    print('impossible')
