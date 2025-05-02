number = int(input('Type a number to see if it is an odd number: \n'))

primo = True

for i in range(2, number):
    if number % i == 0:
        primo = False
        break

if primo:
    print('Primo')
else:
    print('Não é primo')