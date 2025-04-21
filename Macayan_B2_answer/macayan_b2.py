import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = df.rename(str.lower, axis='columns').rename(columns={" ":"_"})
print(output)

output.to_csv("b2_output1.csv")