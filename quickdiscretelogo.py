#Quick calculator for testing diffie-hellman

g = int(input('g: '))
p = int(input('p: '))
y = int(input('y: '))
print('key-y:')
print(g**y%p)

keyx = int(input('key-x: '))
print(keyx**y%p)