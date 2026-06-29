import numpy as np
import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'labels' : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}
x=pd.DataFrame(exam_data)
print(x)
print(x.loc[0:2])
p=x.dropna(inplace=True)
print(p)
e=x[["name" ,"score"]]
print(e)
k={'name': "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}
b=pd.DataFrame(k, index=[0])
y=pd.concat([x,b])
print(y)
s=y.drop("attempts", axis=1)
print(s)
x['sucsess'] = np.where(x['score'] > 10.0, 1, 0)

print(x)

