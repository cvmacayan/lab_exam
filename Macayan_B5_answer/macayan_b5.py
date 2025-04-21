import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = pd.DataFrame((df.groupby(by="Scientific Name")).agg({'Size Est (cm)' : ['mean']}))
print(output)

output.to_csv("b5_output1.csv")