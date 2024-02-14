import pandas as pd
import re

def mapConstructor(word, tb):
    mapList = [x for x in tb if word in x]
    if len(mapList) == 1:
        mapSeries = pd.Series(data=tb[tb.index(mapList[0])+1:])
    else:
        mapSeries = pd.Series(data=tb[tb.index(mapList[0])+1:tb.index(mapList[1])-1])
    mapSeries = mapSeries.str.split(expand=True).rename(columns={0:'Dest',1:'Src',2:'Rng'}).astype(float)
    mapSeries['SrcEnd'] = mapSeries.Src + mapSeries.Rng 
    mapSeries['Shift'] = mapSeries.Dest - mapSeries.Src
    return mapSeries.drop(columns=['Dest', 'Rng'])

def findMapper(mapper, x):
    return list(mapper.loc[(mapper.Src <= x) & (mapper.SrcEnd >= x)].Shift)

tb = list(open('T:/SideProjects/AdventOfCode/2023-05/Input.csv', mode='r'))

seedList = pd.DataFrame(data=re.findall(pattern=' (\d+)',string=tb[0]), columns=['Seed']).astype(float)

cats = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

for cat in cats:
    mapper = mapConstructor(cat, tb)
    seedList['Next'] = seedList.Seed.apply(lambda x: findMapper(mapper, x))
    seedList['Seed'] = seedList.apply(lambda x: x.Seed if len(x.Next) == 0 else x.Next[0] + x.Seed, axis = 1)

#Problem 1 solution
print(seedList.Seed.min())

seedList = pd.DataFrame(data=re.findall(pattern=' (\d+) (\d+)',string=tb[0]), columns=['SeedStart', 'SeedRange']).astype(float)
seedList['SeedEnd'] = seedList.SeedStart + seedList.SeedRange
seedList = seedList.drop(columns=['SeedRange'])

df = pd.DataFrame(columns=['Src', 'SrcEnd', 'Shift'])

for cat in cats:
    mapper = mapConstructor(cat, tb)
    newSeedList = seedList.iloc[0:0]
    #print(mapper)
    for i, row in seedList.iterrows():
        df = mapper.loc[(mapper.Src <= row.SeedStart) & (row.SeedStart <= mapper.SrcEnd)] #Ranges around seed start
        df = df.append(mapper.loc[(row.SeedStart <= mapper.Src) & (mapper.SrcEnd <= row.SeedEnd)]) #Ranges between seed range
        df = df.append(mapper.loc[(mapper.Src <= row.SeedEnd) & (row.SeedEnd <= mapper.SrcEnd)]) #Ranges around seed end
        df = df.append(mapper.loc[(mapper.Src <= row.SeedStart) & (row.SeedEnd <= mapper.SrcEnd)]) #Ranges around seed range
        df = df.drop_duplicates().sort_values(by='Src')
        if len(df) == 0:
            newSeedList = newSeedList.append(row)
        else:
            if df.Src.min() <= row.SeedStart:
                df.Src.iloc[0] = row.SeedStart
            else:
                df = pd.DataFrame({'Src': row.SeedStart, 'SrcEnd': df.Src.min(), 'Shift': 0}, index=[0]).append(df)
            if row.SeedEnd <= df.SrcEnd.max():
                df.SrcEnd.iloc[-1] = row.SeedEnd
            else:
                df = df.append(pd.DataFrame({'Src': df.SrcEnd.max(), 'SrcEnd': row.SeedEnd, 'Shift':0}, index=[0]))
            df['SeedStart'] = df.Src + df.Shift 
            df['SeedEnd'] = df.SrcEnd + df.Shift 
            newSeedList = newSeedList.append(df[['SeedStart', 'SeedEnd']])
    seedList = newSeedList

#Problem 2 solution
print(seedList.SeedStart.min())