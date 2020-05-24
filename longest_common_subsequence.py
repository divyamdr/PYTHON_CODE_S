#code
def longest_common_subsequence(x,y):
    x_len=len(x)
    y_len=len(y)
    matrix=[]
    for i in range(x_len+1):
        d=[0]*(y_len+1)
        matrix.append(d)
    #print(matrix)
    count=0
    for i in range(1,x_len+1):
        for j in range(1,y_len+1):
            if i==1:
                if x[i-1]==y[j-1]:
                    matrix[i][j]=1
                    continue
            else:
                if x[i-1]==y[j-1] and matrix[i-1][j-1]>=1:
                    print(x[i-1],y[j-1])
                    matrix[i][j]=matrix[i-1][j-1]+1
                    count+=1
                elif x[i-1]==y[j-1]:
                    #print(x[i-1],y[j-1])
                    matrix[i][j]=1
                    count=1
                else:
                    matrix[i][j]=max(matrix[i][j-1],matrix[i-1][j])
    return count
t=int(input())
while(t):
    t-=1
    m,n=input().split()
    a=input()
    b=input()
    print(longest_common_subsequence(a,b))
