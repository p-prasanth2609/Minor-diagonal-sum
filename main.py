r = int(input())
c = int(input())
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        element = int(input())
        row.append(element)
    matrix.append(row)
sum=0
i=0
j=c-1
while i<r and j>=0:
    sum+=matrix[i][j]
    i+=1
    j-=1
print(sum)
