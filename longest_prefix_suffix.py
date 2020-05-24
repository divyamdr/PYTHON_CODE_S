def prefixsuffix(s) : 
    n = len(s)
    for index in range(n // 2, 0, -1) : 
        pre = s[0: index] 
        suf = s[n - index: n] 
          
        if (pre == suf) : 
            return index+1 
    return 0
      
s = input()
print(prefixsuffix(s)) 