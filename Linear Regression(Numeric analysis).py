matrix = [[0]*5 for i in range(4)]
print("Enter 5 value of x :")
for i in range(5):
    matrix[0][i]= int(input())
print("Enter 5 value of y :")
for i in range(5):
    matrix[1][i]= int(input())
for i in range(5):
    matrix[2][i] = matrix[0][i] * matrix[1][i]
    matrix[3][i] = matrix[0][i] * matrix[0][i]

sumX ,sumY,sumXY,sumX2 = 0,0,0,0
for i in range(5):
    sumX += matrix[0][i]
    sumY += matrix[1][i]
    sumXY += matrix[2][i]
    sumX2 += matrix[3][i]

aveX ,aveY,aveXY,aveX2 = sumX/5 ,sumY/5,sumXY/5,sumX2/5

m = (aveX*aveY - aveXY)/(aveX*aveX - aveX2)
C = aveY - m * aveX
Rup,Rdn = 0,0
for i in range(5):
    y = m * matrix[0][i] + C
    Rup+= (y - aveY)*(y - aveY)
    Rdn+= (matrix[1][i]- aveY)*(matrix[1][i]- aveY)

R2 = Rup/Rdn
for i in range(5):
    num = input('Enter a number for guess : ')
    num = int(num)
    y =  m *num + C
    print("Probably the output is :", round(y,2))

print('The R-Squared Value is :',round(R2,2))