import string
import copy
import os
from sympy import Symbol
from sympy.solvers import solve

clear = lambda: os.system('cls')

matrices = {"dimensions" : [[[0, 0], [0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
"alphabet" : list(string.ascii_uppercase)
            }

#---------------------------------------------------------------------------------------------------------------------------------

basematrixtwo = [["A", "B"], ["C", "D"]]
basematrixthree = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
solutionmatrixtwo = matrices["dimensions"][0]
solutionmatrixthree = matrices["dimensions"][1]
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
    clear()
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
    
    clear()
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
    
    clear()
    visualmatrixthree(MatrixCore)
    print("The determinant of this matrix is : " + str(determinantthree))
    if len(solutionsthree) == 1:
         print("The Eigenvalue is: " + str(solutionsthree[0]))
    elif len(solutionsthree) == 2:
         print("The Eigenvalues are: " + str(solutionsthree[0]) + " and " + str(solutionsthree[1]))
    else:
        print("The Eigenvalues are: " + str(solutionsthree[0]) + " , " + str(solutionsthree[1]) + " and " + str(solutionsthree[2]))
#---------------------------------------------------------------------------------------------------------------------------------
def matricestwoadd():
   T = int(input("How many matrices do you want to add? (up to 26) : "))
   totaladdtwo = T
   count = 1
   
   while T > 0:
       clear()
       print(basematrixtwo[0])
       print(basematrixtwo[1])
       row = 0
       print("Matrix #" +str(count))
       while row <= 1:
           col = 0
           while col <= 1:
               matrices["alphabet"][T - 1][row][col] = int(input("Enter a Value for " + str(basematrixtwo[row][col] + " : ")))
               col += 1
           row += 1
       print("")
       T -= 1
       count += 1
    
   while totaladdtwo > 0:
       z = 0
       while z <= 1:
           g = 0
           while g <= 1:
               solutionmatrixtwo[z][g] += (matrices["alphabet"][totaladdtwo - 1][z][g])
               g += 1
           z += 1
       totaladdtwo -= 1   
       
   print("")
   print("The resulting matrix is: ")
   print(solutionmatrixtwo[0])
   print(solutionmatrixtwo[1])
#---------------------------------------------------------------------------------------------------------------------------------
def matricesthreeadd():
   T = int(input("How many matrices do you want to add? (up to 26) : "))
   totaladdthree = T
   count = 1
   
   while T > 0:
       clear()
       print(basematrixthree[0])
       print(basematrixthree[1])
       print(basematrixthree[2])
       print("Matrix #" +str(count))
       row = 0
       while row <= 2:
           col = 0
           while col <= 2:
               matrices["alphabet"][T - 1][row][col] = int(input("Enter a Value for " + basematrixthree[row][col] + " : "))
               col += 1
           row += 1 
       print("")
       T -= 1
       count += 1
    
   while totaladdthree > 0:
       z = 0
       while z <= 2:
           g = 0
           while g <= 2:
               solutionmatrixthree[z][g] += (matrices["alphabet"][totaladdthree - 1][z][g])
               g += 1
           z += 1
       totaladdthree -= 1   
       
   print("")
   print("The resulting matrix is: ")
   print(solutionmatrixthree[0])
   print(solutionmatrixthree[1])
   print(solutionmatrixthree[2])
#---------------------------------------------------------------------------------------------------------------------------------    
def matricestwosubtract():
   T = int(input("How many matrices do you want to subtract? (up to 26) : "))
   totalsubtwo = T
   tsub = T
   count = 1

   while T > 0:
       clear()
       print(basematrixtwo[0])
       print(basematrixtwo[1])
       print("Matrix #" +str(count))
       row = 0
       while row <= 1:
           col = 0
           while col <= 1:
               matrices["alphabet"][T - 1][row][col] = int(input("Enter a Value for " + str(basematrixtwo[row][col] + " : ")))
               col += 1
           row += 1
       print("")
       T -= 1
       count += 1
   
   while tsub != -2:
       if totalsubtwo == tsub:
           z = 0
           while z <= 1:
               g = 0
               while g <= 1:
                   solutionmatrixtwo[z][g] = (matrices["alphabet"][totalsubtwo - 1][z][g])
                   g += 1
               z += 1
           tsub = 0
           totalsubtwo -= 1
       else:
           while totalsubtwo > 0:
               z = 0
               while z <= 1:
                   g = 0
                   while g <= 1:
                       solutionmatrixtwo[z][g] -= (matrices["alphabet"][totalsubtwo - 1][z][g])
                       g += 1
                   z += 1
               totalsubtwo -= 1
           tsub = -2
       
   print("")
   print("The resulting matrix is: ")
   print(solutionmatrixtwo[0])
   print(solutionmatrixtwo[1])
#-------------------------------------------------------------------------------------------------------------------------------   
def matricesthreesubtract():
   T = int(input("How many matrices do you want to subtract? (up to 26) : "))
   totalsubthree = T
   tsub = T
   count = 1

   while T > 0:
       clear()
       print(basematrixthree[0])
       print(basematrixthree[1])
       print(basematrixthree[2])
       print("Matrix #" +str(count))
       row = 0
       while row <= 2:
           col = 0
           while col <= 2:
               matrices["alphabet"][T - 1][row][col] = int(input("Enter a Value for " + str(basematrixtwo[row][col] + " : ")))
               col += 1
           row += 1
       print("")
       T -= 1
       count += 1
   
   while tsub != -2:
       if totalsubthree == tsub:
           z = 0
           while z <= 2:
               g = 0
               while g <= 2:
                   solutionmatrixtwo[z][g] = (matrices["alphabet"][totalsubthree - 1][z][g])
                   g += 1
               z += 1
           tsub = 0
           totalsubthree -= 1
       else:
           while totalsubthree > 0:
               z = 0
               while z <= 2:
                   g = 0
                   while g <= 2:
                       solutionmatrixtwo[z][g] -= (matrices["alphabet"][totalsubthree - 1][z][g])
                       g += 1
                   z += 1
               totalsubthree -= 1
           tsub = -2
       
   print("")
   print("The resulting matrix is: ")
   print(solutionmatrixthree[0])
   print(solutionmatrixthree[1])
   print(solutionmatrixthree[2])
#---------------------------------------------------------------------------------------------------------------------------------
def askadd():
    usertype = input('''Which type of matrix do you want to add? :
    a: 2x2 matrix
    b: 3x3 matrix 
    ''')
    
    if usertype == 'a':
        for y in range(26):
            matrices["alphabet"][y] = copy.deepcopy(matrices["dimensions"][0])
        matricestwoadd()
    elif usertype == 'b':
        for y in range(26):
            matrices["alphabet"][y] = copy.deepcopy(matrices["dimensions"][1])
        matricesthreeadd()
    

#---------------------------------------------------------------------------------------------------------------------------------
def asksubtract():
    usertype = input('''Which type of matrix do you want to subtract? :
    a: 2x2 matrix
    b: 3x3 matrix 
    ''') 
    
    if usertype == 'a':
        for y in range(26):
            matrices["alphabet"][y] = copy.deepcopy(matrices["dimensions"][0])
        matricestwosubtract()
    elif usertype == 'b':
        for y in range(26):
            matrices["alphabet"][y] = copy.deepcopy(matrices["dimensions"][1])
        matricesthreesubtract()
    
#---------------------------------------------------------------------------------------------------------------------------------
def eigen():
    clear()
    T = int(input("How many matrices do you want to investigate?: "))
    clear()
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
#-----------------------------------------------------------------------------------------------------------------------------------

def start():
   question = input('''What do you want to do? :
    a: Investigate Eigenvalues and Determinant
    b: Add matrices
    c: Subtract matrices
''')

   if question == 'a':
      eigen()
   elif question == 'b':
      askadd()
   elif question == 'c':
      asksubtract()
   else:
      print('Please enter either a,b or c')
      
#This calls the procedure 'start', which starts the program:
start()
