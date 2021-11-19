m=int(input('enter m(row): '))
n=int(input('enter n(col): '))
p=int(input('enter p(row): '))
q=int(input('enter q(col): '))

a=[]
b=[]
    
for i in range(m):
    col = []
    for j in range(n):
        num=int(input('Enter the numbers: '))
        col.append(num)
    a.append(col)
print("First Matrix: ",a)

for i in range(p):
    col = []
    for j in range(q):
        num=int(input('Enter the numbers: '))
        col.append(num)
    b.append(col)
print("Second Matrix: ",b)

def sparse_mat(matrix,m,n):
    s=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!= 0 :
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                s.append(temp)
                s[0][0] = m
                s[0][1] = n
    return s           
def add(s1,s2):
    i = 1
    j = 1
    k = 1
    s3 = []
    if ((s1[0][0] == s2[0][0]) and (s1[0][1] == s2[0][1])):
        while ((i <= s1[0][2]) and (j <= s2[0][2])):            
            if (s1[i][0] == s2[j][0]):
                temp =[]
                if (s1[i][1] == s2[j][1]):
                    temp.append(s1[i][0])
                    temp.append(s1[i][1])
                    temp.append(s1[i][2]+s2[j][2])
                    s3.append(temp)
                    i += 1
                    j += 1
                    k += 1
                elif (s1[i][1]<s2[j][1]):
                    temp.append(s1[i][0])
                    temp.append(s1[i][1])
                    temp.append(s1[i][2])
                    s3.append(temp)
                    i += 1
                    k += 1
                else:
                    temp.append(s2[j][0])
                    temp.append(s2[j][1])
                    temp.append(s2[j][2])
                    s3.append(temp)
                    j += 1
                    k += 1                    
            elif (s1[i][0]<s2[j][0]):
                temp =[]
                temp.append(s1[i][0])
                temp.append(s1[i][1])
                temp.append(s1[i][2])
                s3.append(temp)
                i +=1
                k +=1
            else:
                temp =[]
                temp.append(s1[j][0])
                temp.append(s1[j][1])
                temp.append(s1[j][2])
                s3.append(temp)
                j +=1
                k +=1

        while (i <= s1[0][2]): 
            temp = []
            temp.append(s1[i][0])
            temp.append(s1[i][1])
            temp.append(s1[i][2])
            s3.append(temp)
            i += 1
            k += 1
        while (j <= s2[0][2]):
            temp = []
            temp.append(s2[j][0])
            temp.append(s2[j][1])
            temp.append(s2[j][2])
            s3.append(temp)            
            j += 1
            k += 1            
       
        s3.insert(0,[s1[0][0],s1[0][1],k-1])
    else:
        print("\n Addition is not possible")
        
    print("Addition of Sparse Matrix : ")
    print("\nRow  Col  Value")
    for row in s3: 
        for element in row: 
            print(element, end ="    ") 
        print() 


c=sparse_mat(matrix=a,m=m,n=n)
print("First sparse matrix : ",c)
d=sparse_mat(matrix=b,m=p,n=q)
print("Second sparse matrix : ",d)
add(c,d)
