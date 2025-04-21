import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",")
output = df[['Count', 'Size Est (cm)']].fillna(0)
print(output)

output.to_csv("b10_output1.csv")