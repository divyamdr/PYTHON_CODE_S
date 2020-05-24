"""
Mr. X is teaching number theory in his class. He is discussing about factors and permutations in his class. A factor of a positive integer N is a positive integer that divides n precisely (without leaving a remainder). The set of factors always includes 1 and N. Mr. X likes combinatorics a lot. He asked his students find out all the factors of the number Y, and sort them in an ascending order. He asks them to list all permutations of the factors. They then need to cross out all permutations where two adjacent numbers are adjacent in the same order in the original list. The number of uncrossed (valid) permutations are to be given to him.

Illustration:
Integer 9 has 3 factors [1,3,9].
The permutations of these factors of number 9 are [1,3,9],[1,9,3],[3,9,1], [3,1,9], [9,1,3],[9,3,1].
Of these 6 permutations, we need to cross out [1,3,9] (1 3 adjacent in same order), [3,9,1] (3 9 in same order) and[9,1,3] (1 3 in same order) The remaining (valid) permutations are:
[1,9,3] ,[9,3,1],[3,1,9] Hence the number of valid permutations =3, which is the answer.

Constraints:
1<= N<=120000
1<=T<= 100

Input:

The first line contains T, the number of testcases
Next T lines contain the integer N


Output:

T lines containing number of valid permutations satisfying conditions mentioned in the problem statement for given input.

Sample Input 1:
1
10

Sample Output 1:
11

Explanation:
T=1 (there is 1 test case)
N=10.
10 has 4 factors [1,2,5,10]. There are 24 permutations of these four factors. The 11 valid permutations are [1,5,2,10],[1,10,5,2], [2,1,10,5], [2,10,1,5], [2,10,5,1], [5,1,10,2], [5,2,1,10], [5,2,10,1], [10,1,5,2], [10,2,1,5], [10,5,2,1]. Hence the output is 11.
"""
def factor(n):
    count=1
    for i in range(1,(n//2)+1):
        if n%i==0:
            count+=1
    return count
def factorial(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res
t=int(input())
while(t):
    t-=1
    n=int(input())
    n=factor(n)
    res=(n-1)*(factorial(n-2)*(n-1))
    #print(res)
    final=0
    for i in range(3,n):
        final+=i*(n-i+1)
        #print(i*(n-i))
    print(res-final-1)
