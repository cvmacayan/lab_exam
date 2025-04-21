import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = df.drop_duplicates(subset=['Date','Site','Scientific Name'])
print(output)

output.to_csv("b11_output1.csv")