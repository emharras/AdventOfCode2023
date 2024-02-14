import pandas as pd 

def winningCardList(cardRow, maxCardNum):
    return list(range(cardRow.CardNum + 1, min(cardRow.CardNum + cardRow.Winners + 1, maxCardNum)))


df = pd.read_csv('T:/SideProjects/AdventOfCode/2023-04/Input1.csv', names=['Card'])

df['CardNum'] = df.Card.str.extract(pat='Card[ ]+(\d+):.*').astype(int)

maxCardNum = df.CardNum.max()

df['Winners'] = df.Card.str.extract(pat='Card[ ]+\d+: ([\d ]+) \|.*')
df['Winners'] = df.Winners.str.split()

df['Testers'] = df.Card.str.extract(pat='.*\| ([\d ]+)$')
df['Testers'] = df.Testers.str.split()

df = df.explode('Testers').explode('Winners')

df = df.loc[df.Winners == df.Testers]

df = df.groupby('CardNum').Winners.count().reset_index()

df['Points'] = pow(2, df.Winners-1)

#Problem 1 solution
print(df.Points.sum())

df['NextCards'] = df.apply(lambda x: winningCardList(x, maxCardNum+1), axis=1)

dfExpand = df.explode('NextCards').NextCards

cardCount = maxCardNum + len(dfExpand)

while True:
    dfExpand = pd.merge(dfExpand, df, left_on='NextCards', right_on='CardNum')
    dfExpand = dfExpand.explode('NextCards_y').NextCards_y.rename("NextCards")
    if len(dfExpand) == 0:
        break
    cardCount += len(dfExpand)

print(cardCount)