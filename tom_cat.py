def function(n,k):
    result=0
    if n>=k and n>=0 and k<=10**14:
        factorial=[0]*(n+1)
        factorial[0]=1
        for i in range(1, n + 1):
            factorial[i] = i * factorial[i - 1]
        #print(factorial)
        for i in range(k+1):
            if i%2==0:
                #print(i,result)
                result+=int(factorial[n]/(factorial[n-i]*factorial[i]))
        result=result%1000000007
    return result
n,k=map(int,input().split())
print(function(n,k))
