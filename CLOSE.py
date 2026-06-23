import numpy as np
x=(int(input("enter number of students")))
a=(int(input("enter number of subjects")))
MARKSarray=np.zeros((x,a))
print(MARKSarray)
for i in range(x):
    print("/n enter the marks ")
    for l in range(a):
        MARKSarray[i,l]=float(input("enter the marks"))
totalmarks=np.sum(MARKSarray, axis=1)
persontage=(totalmarks/(a*100))*100
grade=""
for y in range(x):
    p=persontage[i]
    if p >= 90:
        grade="A+"
    elif p >= 80:
        grade="A"
    elif p >=70:
        grade="B+"
    elif p>= 60:
        grade="B"
    elif p>= 50:
        grade= "c"
    else:
        grade="F"
    print(grade)