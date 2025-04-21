import pandas as pd

df = pd.read_csv("Exam_Table.csv", sep=",").dropna()
output = df["Observer"].unique()
output2 = pd.DataFrame({"unique observers" : [output]})
print(output2)

output2.to_csv("b7_output1.csv", index=False)