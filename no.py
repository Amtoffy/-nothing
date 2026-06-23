import numpy as np 
I=0
x=np.zeros(5)
while I < 5 :
    A=(int(input("enter 5 grades BETWEEN 0 and 100")))
    
    x[I]=A
    I=I+1
print(x)
x[2]= 85
print(x)