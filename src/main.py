import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Find top students')
parser.add_argument('filename', metavar='F', type=str)
parser.add_argument('percentage', metavar='F', type=int)
args = parser.parse_args()
filename = args.filename
percentage = args.percentage


df = pd.read_csv(filename)
df1 = df.iloc[:, [0, 1, 3, 5]]
df1['final'] = df1.apply(lambda x: (x[1]+x[2]+2*x[3])/400, axis=1)
indicies = df1.final.argsort()
num_students = int(len(df)*(percentage/100))
filtered_students = df1.iloc[indicies[-num_students:]][::-1]
ids = filtered_students.student_id.values
print(ids)
