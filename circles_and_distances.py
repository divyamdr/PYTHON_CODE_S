import math
def function(vel1,vel2,rad1,rad2,time):
    x1=(vel1*time*math.pi)/180
    x2=(vel2*time*math.pi)/180
    s=round(math.sqrt(rad1**2+rad2**2-2*rad1*rad2*math.cos(x1-x2)),2)
    s=str(s)
    if s[-2]=='.':
        print(s+'0')
    else:
        print(s)
vel1=int(input())
rad1=int(input())
vel2=int(input())
rad2=int(input())
time=int(input())
function(vel1,vel2,rad1,rad2,time)