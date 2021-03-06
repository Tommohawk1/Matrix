import string
import copy


matrices = {"dimensions" : [[[0, 0], [0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]],
"alphabet" : list(string.ascii_uppercase)
            }


basematrix = [["A", "B"], ["C", "D"]]
solutionmatrixtwo = matrices["dimensions"][0]

def start():
    usertype = input('''Which type of matrix do you want to add? :
    a: 2x2 matrix
    b: 3x3 matrix 
    ''')
    
    if usertype == 'a':
        for y in range(25):
            matrices["alphabet"][y] = copy.deepcopy(matrices["dimensions"][0])
    elif usertype == 'b':
        for y in range(25):
            matrices["alphabet"][y] = matrices["dimensions"][1]

def matricestwo():
   T = int(input("How many matrices do you want to add? (up to 26) : "))
   totaladd = T

   while T > 0:
       row = 0
       while row <= 1:
           col = 0
           while col <= 1:
               matrices["alphabet"][T - 1][row][col] = int(input("Enter a Value for " + str(matrices["alphabet"][T-1][row][col]) + " : "))
               col += 1
           row += 1 
       T -= 1
    
   while totaladd > 0:
       z = 0
       while z <= 1:
           g = 0
           while g <= 1:
               solutionmatrixtwo[z][g] += (matrices["alphabet"][totaladd - 1][z][g])
               print(matrices["alphabet"][totaladd - 1][z][g])
               g += 1
           z += 1
       totaladd -= 1   
      
      
        
       
start()

matricestwo()

print(matrices["alphabet"][1])
print(matrices["alphabet"][0])
print(solutionmatrixtwo)
