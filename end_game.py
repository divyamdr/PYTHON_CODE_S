#Code goes here!
d,h= map(int, input().split())
if d == h:
	print(d)
elif d == 0 or h == 0:
	print(-1)
else:
    if d > h:
	    d, h = h,d
    ans=0
    while d > 0:
        while d * 2 <= h:
            ans += 1
            d *= 2
        ans += 1
        d -= 1
        h -= 1
    print(ans)