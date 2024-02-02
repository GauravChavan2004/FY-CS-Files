



m1=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ]
m2=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ]
m3=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ]
print("Enter 9 elements of first Matrix\n")
for i in range(0,3):
    for j in range(0,3):
        print("Enter Next Int No\n")
        m1[i][j]=int(input("Enter no\n"))

print("Enter 9 elements of Second Matrix\n")
for i in range(0,3):
    for j in range(0,3):
        print("Enter Next Int No\n")
        m2[i][j]=int(input("Enter no\n"))

for i in range(0,3):
    for j in range(0,3):
        m3[i][j]=0
        for k in range(0,3):
            m3[i][j]+=m1[i][k]*m2[k][j]
print("\nResultant Matrix\n")
for i in range(0,3):
    for j in range(0,3):
        print(m3[i][j] ,end="\t")
    print("\n")

