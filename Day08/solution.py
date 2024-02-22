import pandas as pd
import re
import math

def steps(c, z, df, pattern):
    patLen = len(pattern)
    patIt = 0
    stp = 0

    while c != z:
        if patIt == patLen:
            patIt = 0

        if pattern[patIt] == 'L':
            c = df.L.loc[c]
        else:
            c = df.R.loc[c]
        
        patIt += 1
        stp += 1
    
    return stp

def stepsLastChar(c, z, df, pattern):
    patLen = len(pattern)
    patIt = 0
    stp = 0

    while c[-1] != z:
        if patIt == patLen:
            patIt = 0

        if pattern[patIt] == 'L':
            c = df.L.loc[c]
        else:
            c = df.R.loc[c]
        
        patIt += 1
        stp += 1
    
    return stp


tb = list(open('T:/SideProjects/AdventOfCode/2023-08/Input.csv', mode='r'))

pattern = tb[0].strip()

df = pd.DataFrame(data=tb[2:], columns=['SourceData'])
df[['Coord', 'L', 'R']] = df.SourceData.str.extract(pat='^"(\w{3}) = \((\w{3}), (\w{3})\)')
df = df.set_index('Coord', drop=False).drop(columns=['SourceData'])

c = 'AAA'

stp = steps(c, 'ZZZ', df, pattern)

#Problem 1 solution
print(stp)

#Solution based on this post: https://todd.ginsberg.com/post/advent-of-code/2023/day8/

c = df.loc[(df.Coord.str.get(-1) == 'A')].copy()

c['Steps'] = c.Coord.apply(lambda x: stepsLastChar(x, 'Z', df, pattern))

lcm = c.Steps.iloc[0]
for i in range(len(c)-1):
    lcm = (lcm*c.Steps.iloc[i+1])//math.gcd(lcm, c.Steps.iloc[i+1])

#Problem 2 solution
print(lcm)