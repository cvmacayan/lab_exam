import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = df.query('Genus.str.startswith("Pomacentrus")', engine="python")
print(output)

output.to_csv("b3_output1.csv", index=False)