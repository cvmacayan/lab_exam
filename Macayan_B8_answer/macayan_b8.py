import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",")
output = df.query('`Visibility (m)` > 8')
print(output)

output.to_csv("b8_output1.csv", index=False)