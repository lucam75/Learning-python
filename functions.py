def sayHello(name='anonymous'):
    print(f'Hello {name}')

sayHello('world')
sayHello('Luis')
sayHello()

add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(10, 30))