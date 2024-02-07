import pandas as pd
import re

df = pd.read_csv('T:/SideProjects/AdventOfCode/2023-01/Input1.csv', names=['Val'])
#calib = pd.read_csv('T:/SideProjects/AdventOfCode/2023-01/TestInput.csv', names=['Val'])

df1 = df.Val.str.replace('(\D)+', '')
df1 = df1.apply(lambda x: int(x[0] + x[-1]))

print('First answer')
print(df1.sum())

numDict = {'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'}

pattern = '|'.join(x for x in numDict)
df['FirstDigit'] = df.Val.str.extract('(' + pattern + '|\d)')
df['LastDigit'] = df.Val.apply(lambda x: x[::-1]).str.extract('(' + pattern[::-1] + '|\d)')
df['LastDigit'] = df.LastDigit.apply(lambda x: x[::-1])
df = df[['FirstDigit', 'LastDigit']].replace(to_replace=numDict, regex=True)
df = df.FirstDigit + df.LastDigit
df = df.astype(int)

print('Second answer')
print(df.sum())