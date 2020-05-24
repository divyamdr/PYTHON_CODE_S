"""
Vikrant is at his college’s fest, and being a true foodie, he went straight away to the food corner in hope of getting his hands on some delicacies. There are N stalls in the food corner numbered 1 to N, and the ith stall has Ai people standing in front of it. Each stall takes a minute to serve one person. Vikrant will initially join the line for the first stall, but being an impatient guy, he will go on to join the line for the next stall after every minute if he is not served. (If he is in the line for the last stall, he will join the one for the first stall)

You have to tell the food stall from which Vikrant will be served.

Input:
The first line of the input contains T denoting the number of testcases. Each testcase contains two lines of input.
The first line of each testcase consists of a positive integer N. The second line consists of N positive integers A1, A2, …, AN separated by spaces.

Output:
For each testcase, in a new line, print the food-stall that will serve Vikrant.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
0 ≤ Ai ≤ 106

Examples:
Input:
2
4
1 4 2 1
2
4 4
Output:
3
1

Explanation:
Testcase 1: At T = 0, he stands at stall 1, it is occupied till T=1 so he moves so stall 2, where he waits for 1 minute after which he moves to stall 3 at T = 2, which is empty at that point since the 2 people waiting at that stall are already serves by T = 2, so he gets serves at this stall.
Testcase 2: The progression is explained by the states given below.
4 4 T=0
3 3 T=1
2 2 T=2
1 1 T=3
0 0 T=4
"""
t=int(input())
res=0
while(t):
    t-=1
    n=int(input())
    a=[int(x) for x in input().split()]
    i=0
    while a[t%n]>t:
        t+=1
    print((t%n)+1)

