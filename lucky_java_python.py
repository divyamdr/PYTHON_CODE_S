#Code goes here!
def solution(n,k):
    n1=max(n,k)+1
    fact = [0 for i in range(n1)]
    fact[0]=1
    for i in range(1,n1):
        fact[i]=i*fact[i-1]
    return fact[n]*fact[k]
for i in range(int(input())):
    n,k=map(int,input().split())
    print(solution(n,k))