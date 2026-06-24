import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Omar", "Sara", None, "Lina"],
    "Age": [25, 30, None, 30, 28, 200],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "Marketing"],
    "Salary": [50000, 60000, 55000, 60000, None, 70000]
}
x=pd.DataFrame(data)
print(x.info())
print(x.isnull().sum())
p=x["Salary"].mean()
print(p)
c=x.drop_duplicates(inplace=True)
print(c)