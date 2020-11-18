from simplex2 import *

# Spremenljivke so x1,...,x9.
# Zadnji dve vrstici ustrezata enakosti x1 + ... + x9 = 1
# Funkcional je ničeln, saj iščemo vse strategije

A = [
    [0, 2, 2, -3, 0, 0, -4, 0, 0], 
    [-2, 0, 0, 0, 3, 3, -4, 0, 0], 
    [-2, 0, 0, -3, 0, 0, 0, 4, 4], 
    [3, 0, 3, 0, -4, 0, 0, -5, 0], 
    [0, -3, 0, 4, 0, 4, 0, -5, 0], 
    [0, -3, 0, 0, -4, 0, 5, 0, 5], 
    [4, 4, 0, 0, 0, -5, 0, 0, -6], 
    [0, 0, -4, 5, 5, 0, 0, 0, -6], 
    [0, 0, -4, 0, 0, -5, 6, 6, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [-1, -1, -1, -1, -1, -1, -1, -1, -1]
]

b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]
c = [0, 0, 0, 0, 0, 0, 0, 0, 0]

tab = solve(A, b, c)
solutions = findall(tab)
for solution in solutions:
    print(solution[:9])