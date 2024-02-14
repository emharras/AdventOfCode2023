import pandas as pd
import re

df = pd.read_csv('T:/SideProjects/AdventOfCode/2023-03/Input1.csv', names=['Diag'])

maxIndex = len(df)-1
maxLen = len(df.Diag[0])

df['NumLoc'] = df.Diag.apply(lambda x: [(m.start(0), m.end(0), int(m.group(0))) for m in re.finditer('(\d+)', x)])
print(df.head())
coordArray = []

for index, row in df.iterrows():
    for coord in row.NumLoc:
        surround = df[max(0, index-1):min(maxIndex, index+1)+1]
        surround = surround.Diag.apply(lambda x: x[max(0, coord[0]-1):min(maxLen, coord[1]+1)])
        if surround.str.contains(pat='([^\d^.])').max():
            coordArray.append(coord[2])

#part 1 solution
print(sum(coordArray))

df['GearLoc'] = df.Diag.apply(lambda x: [m.start(0) for m in re.finditer('[*]', x)])
df['NumLocUpdate'] = df.NumLoc.apply(lambda x: [(m[0]-1, m[1], m[2]) for m in x])

gearArray = []

for index, row in df.iterrows():
    for coord in row.GearLoc:
        surround = [x for xArray in df.NumLocUpdate[max(0, index-1):min(maxIndex, index+1)+1] for x in xArray]
        surround = [x for x in surround if x[0] <= coord & coord <= x[1]]
        if len(surround) == 2:
            gearArray.append(surround[0][2] * surround[1][2])

#part 2 solution
print(sum(gearArray))
