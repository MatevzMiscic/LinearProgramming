from simplex import *

# Koda je dostopna na https://github.com/MatevzMiscic/LinearProgramming

# Spremenljivke so x1,...,x9.
# Zadnji dve vrstici ustrezata enakosti x1 + ... + x9 = 1
# Funkcional je ničeln, saj iščemo vse strategije.

# To je v resnici linearni program Pi_1, le da je izbrisana spremenljivka w, 
# ker vemo, da je v optimalni rešitvi njena vrednost enaka 0.

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

"""
Izpis:

(0, 0, 16/37, 0, 12/37, 0, 9/37, 0, 0)
(0, 0, 25/61, 0, 20/61, 0, 16/61, 0, 0)
(0, 0, 5/12, 0, 1/3, 0, 1/4, 0, 0)
(0, 0, 20/47, 0, 15/47, 0, 12/47, 0, 0)

"""