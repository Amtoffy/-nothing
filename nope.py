with open("a.txt","r" ) as file:
    x=file.read()
    #print(x)
with open("a.txt","a" ) as file:
    file.write("\nat the end thomorrow never gonna come because its the end lol")

with open("a.txt","r" ) as file:
    x=file.read()
    lis=x.split()
    a={}
    for e in lis:
        if e in a:
            a[e]=+1
        elif e not in a:
            a[e]=1
    print(a)