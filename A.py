import pandas as pd

students = {
    "Name": ["Ali", "Sara", "Omar", "Lina"],
    "Grade": [15, 18, 12, 17],
    "Age": [20, 21, 19, 22]
}
x=pd.DataFrame(students, index=["a", "b","c","d"])
print(x)
print(x.loc["b"])
print(x.iloc[3])
a=x.drop("Age", axis=1)
print(a)