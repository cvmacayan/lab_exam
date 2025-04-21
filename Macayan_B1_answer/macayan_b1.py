import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = pd.DataFrame(df)
print(df)

output.to_csv("b1_output1.csv", index=False)


