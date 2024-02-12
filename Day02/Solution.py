import pandas as pd

df = pd.read_csv('T:/SideProjects/AdventOfCode/2023-02/Input1.csv', names=['Game'])

df['GameNum'] = df.Game.str.extract(pat=r'Game (\d+).*')
df['Sets'] = df.Game.str.split(pat=';', expand = False)

df = df.explode('Sets')

df['Green'] = df.Sets.str.extract(pat=r'.* (\d+) green.*').fillna(0)
df['Blue']  = df.Sets.str.extract(pat=r'.* (\d+) blue.*').fillna(0)
df['Red'] = df.Sets.str.extract(pat=r'.* (\d+) red.*').fillna(0)

df = df.astype({'GameNum': int, 'Green': int, 'Blue': int, 'Red': int})

df = df.groupby(by=['GameNum'])[['Green', 'Blue', 'Red']].max().reset_index(drop = False)

dfFiltered = df[(df.Red <= 12) & (df.Green <= 13) & (df.Blue <= 14)]

#problem 1 solution
print(dfFiltered.GameNum.sum())

df['Power'] = df.Red * df.Green * df.Blue

#problem 2 solution
print(df.Power.sum())
