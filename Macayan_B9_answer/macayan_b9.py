import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = df.groupby(by=["Replicate","Interval"]).agg({'Count' : ['mean']})
print(output)

output.to_csv("b9_output1.csv")