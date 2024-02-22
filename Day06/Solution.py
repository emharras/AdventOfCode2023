import pandas as pd 
import re
import math

def solveQuad(time, dist):
    return (math.floor((-1*time + math.sqrt(pow(time, 2) - 4*dist))/(-2.0))+1, math.ceil((-1*time - math.sqrt(pow(time, 2) - 4*dist))/(-2.0))-1)

tb = list(open('T:/SideProjects/AdventOfCode/2023-06/Input.csv', mode='r'))

df = pd.DataFrame(data={'Time': re.findall(pattern=' (\d+)',string=tb[0]), 'Distance': re.findall(pattern=' (\d+)',string=tb[1])}).astype(int)

df['ChargingTime'] = df.apply(lambda x: solveQuad(x.Time, x.Distance), axis = 1)
df['Range'] = df.ChargingTime.apply(lambda x: x[1] - x[0] + 1)

print(df.Range.prod())

chargingTime = solveQuad(int(''.join(df.Time.astype(str))), int(''.join(df.Distance.astype(str))))

print(chargingTime[1] - chargingTime[0] + 1)