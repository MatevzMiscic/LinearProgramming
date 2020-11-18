from simplex import *

# troprstna mora
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

def printMat(mat):
    for row in mat:
        for a in row:
            print(a, end="  ")
        print()

# zgenerira problem za igro mora
def generate():
    A = [[val(i, j) for j in range(9)] for i in range(9)]
    A.append([1 for i in range(9)] + [0, 0])
    A.append([-1 for i in range(9)] + [0, 0])
    for i in range(9):
        A[i] += [1, -1]
    b = [0 for i in range(9)] + [1, -1]
    c = [0 for i in range(9)] + [1, -1]
    return A, b, c

# zgenerira problem za igro mora, v je nepozitiven
def generate2():
    A = [[val(i, j) for j in range(9)] for i in range(9)]
    A.append([1 for i in range(9)] + [0])
    A.append([-1 for i in range(9)] + [0])
    for i in range(9):
        A[i] += [-1]
    b = [0 for i in range(9)] + [1, -1]
    c = [0 for i in range(9)] + [-1]
    return A, b, c

# zgenerira problem za igro mora, v je nič
def generate3():
    A = [[val(i, j) for j in range(9)] for i in range(9)]
    A.append([1 for i in range(9)])
    A.append([-1 for i in range(9)])
    b = [0 for i in range(9)] + [1, -1]
    c = [0 for i in range(9)]
    return A, b, c
    
A, b, c = generate3()

"""
print("A:")
print("rows:", len(A))
print("cols:", end="  ")
for row in A:
    print(len(row), end="  ")
print()
print("b:", len(b))
print("c:", len(c))
#"""

#"""
tab = solve(A, b, c)
sols = findall(tab)
for sol in sols:
    print(sol[:9])
    #print(sol)
#"""