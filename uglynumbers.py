"""
Ugly Numbers
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.
"""
def ugly_number(n):
    ugly=[0]*n
    ugly[0]=1
    i2,i3,i5=0,0,0
    next_2=2
    next_3=3
    next_5=5
    for i in range(1,n):
        ugly[i]=min(next_2,next_3,next_5)
        if ugly[i] == next_2: 
            i2 += 1
            next_2 = ugly[i2] * 2
  
        if ugly[i] == next_3: 
            i3 += 1
            next_3 = ugly[i3] * 3
  
        if ugly[i] == next_5:  
            i5 += 1
            next_5 = ugly[i5] * 5
  
    # return ugly[n] value 
    return ugly[-1] 
if __name__ == '__main__': 
    n=int(input('enter the nth ugly number'))
    print(ugly_number(n))

