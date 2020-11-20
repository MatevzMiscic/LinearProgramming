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


# vrednost v plačilni matriki
def val(i, j):
    first = (i // 3 + 1, i % 3 + 1)
    second = (j // 3 + 1, j % 3 + 1)
    a = (first[1] == second[0])
    b = (second[1] == first[0])
    value = first[0] + second[0]
    if a == b:
        return 0
    elif a:
        return value
    return -value

# zgenerira problem za igro mora, vemo da bo vrednost igre manjša ali enaka 0
def generate():
    A = [[val(i, j) for j in range(9)] for i in range(9)]
    A.append([1 for i in range(9)] + [0])
    A.append([-1 for i in range(9)] + [0])
    for i in range(9):
        A[i] += [-1]
    b = [0 for i in range(9)] + [1, -1]
    c = [0 for i in range(9)] + [-1]
    return A, b, c

# ta način je hitrejši, saj funkcional ni ničeln in moramo pregledati veliko manj možnosti
A, b, c = generate()
tab = solve(A, b, c)
solutions = findall(tab)
for solution in solutions:
    print(solution[:9])