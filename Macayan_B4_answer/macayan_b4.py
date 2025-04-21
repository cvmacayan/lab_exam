import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = pd.DataFrame(df.groupby(by="Scientific Name").agg({'Count' : ['sum']}))
print(output)

output.to_csv("b4_output1.csv", index=True)