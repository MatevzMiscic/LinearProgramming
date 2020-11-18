class Tableau:
    def __init__(self, A, b, c):
        self.n = len(c)
        self.m = len(b)
        self.in_base = [i >= self.n for i in range(self.n + self.m)]
        self.base = [self.n + i for i in range(self.m)]
        self.table = []
        for i in range(self.m):
            row = A[i][::]
            for j in range(self.m):
                row.append(int(i == j))
            row.append(b[i])
            self.table.append(row)
        row = c[::]
        for i in range(self.m + 1): row.append(0)
        self.table.append(row)

    def base_val(self):
        return -self.table[-1][-1]

    def base_sol(self):
        solution = [0 for i in range(self.n + self.m + 1)]
        solution[-1] = self.base_val()
        for i, var in enumerate(self.base):
            solution[self.base[i]] = self.table[i][-1]
        return tuple(solution)

    def del_var(self, num):
        if self.in_base[num]:
            return False
        for i in range(self.m):
            del self.table[i][num]
            if self.base[i] > num:
                self.base[i] -= 1
        del self.table[self.m][num]
        del self.in_base[num]
        self.n -= 1
        return True

    def express(self, vec):
        for i in range(self.m):
            coef = -vec[self.base[i]]
            for j in range(self.n + self.m + 1):
                vec[j] += coef * self.table[i][j]

    def key(self):
        key = 0
        for i in self.base:
            key |= (1 << i)
        return key

    def entering_rule(self):
        # izberemo vstopajočo spremenljivko
        col = -1
        for i in range(self.n + self.m):
            if not self.in_base[i] and self.table[self.m][i] > 0:
                col = i
                break
        # če ni kandidata vrnemo False
        if col < 0:
            return False
        return col

    def leaving_rule(self, col, row=0):
        # izberemo izstopajočo spremenljivko (oziroma vrstico)
        row = 0
        for i in range(self.m):
            if self.table[i][col] <= 0:
                continue 
            val = self.table[i][-1] / self.table[i][col]
            if self.table[row][col] <= 0 or val < self.table[row][-1] / self.table[row][col]:
                row = i
        # če ni kandidata vrnemo False
        if self.table[row][col] <= 0:
            return False
        return row

    def pivot(self, row, col):
        # če pivot ni pozitiven smo končali
        pivot = self.table[row][col]
        if pivot == 0:
            return False
        # delimo pivotno vrstico
        for i in range(self.n + self.m + 1):
            self.table[row][i] /= pivot
        # odštejemo večkratnik pivotne vrstice ostalim
        for i in range(self.m + 1):
            if i == row: continue
            coef = self.table[i][col]
            for j in range(self.n + self.m + 1):
                self.table[i][j] -= coef * self.table[row][j]
        # spremenimo bazo
        self.in_base[col] = True
        self.in_base[self.base[row]] = False
        self.base[row] = col
        return True

    def iterate(self):
        col = self.entering_rule()
        # če smo končali
        if col is False:
            print("Konec")
            return False
        # če je problem neomejen
        row = self.leaving_rule(col)
        if row is False:
            print("Neomejen problem")
            return False
        return self.pivot(row, col)

    def simplex(self):
        while self.iterate():
            self.print()
            print()

    def tab(self):
        print(self.table)
    def __sign(self, num):
        if num >= 0:
            return " + "
        return " - "
    def print(self):
        for i, k in enumerate(self.base):
            print(f"x{k + 1} = {self.table[i][-1]:.2f}", end="")
            for j in range(self.n + self.m):
                if self.in_base[j]: continue
                coef = -self.table[i][j]
                print(self.__sign(coef) + f"{abs(coef):.2f} * x{j + 1}", end="")
            print()
        val = -self.table[self.m][-1]
        print(f"z  = {val}", end="")
        for j in range(self.n + self.m):
            if self.in_base[j]: continue
            coef = self.table[self.m][j]
            print(self.__sign(coef) + f"{abs(coef):.2f} * x{j + 1}", end="")
        print()

def solve(A, b, c):
    n = len(c)
    m = len(b)
    least = 0
    for i in range(m):
        if b[i] < b[least]:
            least = i
    if b[least] < 0:
        # bdr nedopustna, naredimo dvofazno metodo simpleksov
        for row in A:
            row.append(-1)
        d = [-int(i == n) for i in range(n + 1)]
        tab = Tableau(A, b, d)
        tab.pivot(least, n)
        tab.print()
        tab.simplex()
        if tab.base_val() < 0:
            return "Problem ni dopusten"
        tab.del_var(n)
        for i in range(m + 1): c.append(0)
        tab.express(c)
        tab.table[-1] = c[::]
        tab.print()
        tab.simplex()
    else:
        # bdr dopustna
        tab = Tableau(A, b, c)
        tab.print()
        print()
        tab.simplex()
    return tab

def lsb(n):
    if n == 0:
        return -1
    k = 0
    while n & 1 == 0:
        k += 1
        n >>= 1
    return k

def goto(tab, key):
    curkey = tab.key()
    while curkey != key:
        a = lsb(curkey & ~key)
        b = lsb(key & ~curkey)
        for i, var in enumerate(tab.base):
            if var == a:
                row = i
        tab.pivot(row, b)
        curkey = tab.key()
        
# poišče vse optimalne bdr (ne le tistih do katerih lahko pride simpleks)
def findall(tab):
    """
    # odstranimo spremenljivke, ki bodo zagotovo enake 0
    j = tab.n + tab.m - 1
    while j >= 0:
        if tab.table[tab.m][j] < 0:
            tab.del_var(j)
        j -= 1
    """
    # naredimo dfs po slovarjih
    solutions = set()
    visited = set()
    stack = [tab.key()]
    while stack:
        key = stack.pop()
        if key in visited: continue
        print(len(visited), key)
        visited.add(key)
        goto(tab, key)
        solutions.add(tab.base_sol())
        for j in range(tab.n + tab.m):
            if tab.table[tab.m][j] != 0: continue 
            row = tab.leaving_rule(j)
            if row is False: continue
            newkey = (key & ~(1 << tab.base[row])) | (1 << j)
            if newkey not in visited:
                stack.append(newkey)
    tab.print()
    return solutions





"""
A = [[2, 3, 1], [5, 7, 2], [9, 6, 3]]
b = [6, 3, 8]
c = [2, 1, 7]
t = Tableau(A, b, c)
tab = solve(A, b, c)
#"""
"""
A = [[1, 2], [5, 4]]
b = [6, 20]
c = [1, 1]
tab = solve(A, b, c)
"""

"""
A = [[1, 1, 1], [60, 80, 100], [400, 600, 480]]
b = [50, 5000, 24000]
c = [240, 400, 320]
tab = solve(A, b, c)

sols = findall(tab)
#"""

#"""
A = [[-1, -7, 2], [5, 8, -6], [-9, 1, -2]]
b = [3, 1, 4]
c = [0, -1, 0]
tab = solve(A, b, c)
sols = findall(tab)
#"""

"""
# neomejen
A = [[-1, 0, -2], [-1, -2, 1], [-1, 1, 0], [-1, 0, 1]]
b = [-2, 1, 0, -1]
c = [12, 6, 3]
tab = solve(A, b, c)
#"""

"""
A = [
    [-1, 0, 2, 2, -3, 0, 0, -4, 0], 
    [-1, -2, 0, 0, 0, 3, 3, -4, 0], 
    [-1, -6, -4, -4, -7, -4, -4, -4, 0], 
    [-1, 3, 0, 3, 0, -4, 0, 0, -5], 
    [-1, 0, -3, 0, 4, 0 , 4, 0, -5], 
    [-1, -5, -8, -5, -5, -9, -5, 0, -5], 
    [-1, 10, 10, 6, 6, 6, 1, 6, 6], 
    [-1, 6, 6, 2, 11, 11, 6, 6, 6], 
    [-1, 0, 0, -4, 0, 0, -5, 6, 6], 
    ]
b = [0, 0, -4, 0, 0, -5, 6, 6, 0]
c = [-1, 0, 0, 0, 0, 0, 0, 0, 0]
tab = solve(A, b, c)
sols = findall(tab)
#"""
#T.tab()
#T.print()