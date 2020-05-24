a=input()
vowel=['a','e','i','o','u']
s=''
top=''
for i in range(len(a)):
    if a[i]==' ':
        s+=' '
        top=''
    else:
        if top!='' and a[i] in vowel:
            continue
        elif top!='':
            top=''
            s+=a[i]
        else:
            if top=='' and a[i] in vowel:
                top=a[i]
            s+=a[i]

print(s)