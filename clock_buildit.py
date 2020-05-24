def angle1(hour,mint):
    if (hour < 0 or mint< 0 or hour > 12 or mint > 60): 
            print('0.00')
            return
    if (hour==12): 
        hour=0
    if(mint==60): 
        mint=0
    h_angle=0.5*(hour*60+mint)
    m_angle=6*mint
    angle=abs(h_angle-m_angle)
    #print(angle)
    angle=abs(min(360-angle,angle))
    s=str(angle)
    if s[-2]=='.':
        print(s+'0')
    else:
        print(s)
    
a=int(input())
s=float(input())
result=((a/360)*s)
s=str(result)
hour,mint=s.split('.')
hour=int(hour)
mint=int(mint)*6
angle1(int(hour),int(mint))
