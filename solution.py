from sympy import Symbol
from sympy.solvers import solve
import os

clear = lambda: os.system('cls')

twobytwo = [["A", "B"], ["C", "D"]]
threebythree = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
#---------------------------------------------------------------------------------  
def printtwo():
    print(twobytwo[0])
    print(twobytwo[1])
#---------------------------------------------------------------------------------  
def printthree():
    print(threebythree[0])
    print(threebythree[1])
    print(threebythree[2])
#---------------------------------------------------------------------------------  
def matrixtypefirst():
    c = input('''What is the size of the matrix?
    a : 2x2 matrix
    b : 3x3 matrix
    ''')
    return c
#---------------------------------------------------------------------------------  
def visualmatrixtwo(a):
    print(a[0])
    print(a[1])
def visualmatrixthree(b):
    print([b[0]])
    print([b[1]])
    print([b[2]])
    
#---------------------------------------------------------------------------------    
#2x2 matrix procedure
def matrixtwoprocess():    
    i = 0
    while i <= 1:
        x = 0
        while x <= 1 :
            clear()
            printtwo()
            A = int(input("Enter a Value for " + twobytwo[i][x] + " : "))
            twobytwo[i][x] = A
            x += 1
        i += 1    
    MatrixCore = [[twobytwo[0][0], twobytwo[0][1]], 
                  [twobytwo[1][0], twobytwo[1][1]]]
    
    x = Symbol('x')
    Ae = MatrixCore[0][0] - x
    Be = MatrixCore[0][1]
    Ce = MatrixCore[1][0]
    De = MatrixCore[1][1] - x
    
    determinanttwo = (MatrixCore[0][0] * MatrixCore[1][1]) - (MatrixCore[0][1] * MatrixCore[1][0])
    
    print ("")
    visualmatrixtwo(MatrixCore)
    print ("")
    print("The determinant of this matrix is: " + str(determinanttwo))
    solutionstwo = solve((Ae * De) - (Be * Ce))
    print("The Eigenvalues are: " + str(solutionstwo[0]) + " and " + str(solutionstwo[1]))

#-----------------------------------------------------------------------------------
#3x3 matrix procedure
def matrixthreeprocess():
    i = 0
    while i <= 2:
        x = 0
        while x <= 2 :
            clear()
            printthree()
            A = int(input("Enter a Value for " + threebythree[i][x] + " : "))
            threebythree[i][x] = A
            x += 1
        i += 1    
    MatrixCore = [[threebythree[0][0], threebythree[0][1], threebythree[0][2]],
                  [threebythree[1][0], threebythree[1][1], threebythree[1][2]],
                  [threebythree[2][0], threebythree[2][1], threebythree[2][2]]]
    
    determinantthree = { ((MatrixCore[0][0] * MatrixCore[1][1] * MatrixCore[2][2]) + 
                        (MatrixCore[0][1] * MatrixCore[1][2] * MatrixCore[2][0]) + 
                        (MatrixCore[0][2] * MatrixCore[1][0] * MatrixCore[2][1])) - 
                        ((MatrixCore[0][1] * MatrixCore[1][0] * MatrixCore[2][2]) + 
                        (MatrixCore[0][0] * MatrixCore[1][2] * MatrixCore[2][1]) + 
                        (MatrixCore[0][2] * MatrixCore[1][1] * MatrixCore[2][0]))
                        }
    x = Symbol('x')
    Ae = (-1 * threebythree[0][0]) + x
    Be = (-1 * threebythree[0][1])
    Ce = (-1 * threebythree[0][2])
    De = (-1 * threebythree[1][0])
    Ee = (-1 * threebythree[1][1]) + x
    Fe = (-1 * threebythree[1][2])
    Ge = (-1 * threebythree[2][0])
    He = (-1 * threebythree[2][1])
    Ie = (-1 * threebythree[2][2]) + x
    
    addfirstdiagonal = (Ae * Ee * Ie)
    addseconddiagonal = (Be * Fe * Ge)
    addthirddiagonal = (Ce * De * He)
    subfirstdiagonal = (Be * De * Ie)
    subseconddiagonal = (Ae * Fe * He)
    subthirddiagonal = (Ce * Ee * Ge)
    
    pos = (addfirstdiagonal + addseconddiagonal + addthirddiagonal)
    neg = (subfirstdiagonal + subseconddiagonal + subthirddiagonal)
    
    solutionsthree = solve(pos - neg)
    
    print("")
    visualmatrixthree(MatrixCore)
    print("The determinant of this matrix is : " + str(determinantthree))
    if len(solutionsthree) == 1:
         print("The Eigenvalue is: " + str(solutionsthree[0]))
    elif len(solutionsthree) == 2:
         print("The Eigenvalues are: " + str(solutionsthree[0]) + " and " + str(solutionsthree[1]))
    else:
        print("The Eigenvalues are: " + str(solutionsthree[0]) + " , " + str(solutionsthree[1]) + " and " + str(solutionsthree[2]))
    
    
    
    
#------------------------------------------------------------------------------------
#Main Loop/Data
T = int(input("How many matrices do you want to investigate?: "))
while T != 0:
    e = matrixtypefirst()
    if e == "a":
        print(twobytwo[0])
        print(twobytwo[1])
        print("")
        matrixtwoprocess()
        print("")
        T -= 1
    elif e == "b":
        print(threebythree[0])
        print(threebythree[1])
        print(threebythree[2])
        print("")
        matrixthreeprocess()
        print("")
        T -= 1
    else:
        print ("Please enter 'a' or 'b'...")
