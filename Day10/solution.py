import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.geometry.polygon as poly
import shapely.wkt as wkt

shiftDict = {'|': {'u': (-1, 0, 'u'), 'd': (1, 0, 'd')},
         '-': {'r': (0, 1, 'r'), 'l': (0, -1, 'l')},
         'L': {'l': (-1, 0, 'u'), 'd': (0, 1, 'r')},
         'J': {'d': (0, -1, 'l'), 'r': (-1, 0, 'u')},
         '7': {'r': (1, 0, 'd'), 'u': (0, -1, 'l')},
         'F': {'l': (1, 0, 'd'), 'u': (0, 1, 'r')}}

tb = [x.strip() for x in list(open('T:/SideProjects/AdventOfCode/2023-10/Input.csv', mode='r'))]

s = [x for x in tb if 'S' in x][0]
s = (tb.index(s), s.index('S'))

c = (0, 0, '')

if tb[s[0]-1][s[1]] in ['|', '7', 'F']: #Looking above S
    c = (s[0]-1, s[1], 'u')
elif tb[s[0]][s[1]+1] in ['-', 'J', '7']: #Looking right of S
    c = (s[0], s[1]+1, 'r')
elif tb[s[0]+1][s[1]] in ['|', 'L', 'J']: #Looking below S
    c = (s[0]+1, s[1], 'd')
elif tb[s[0]][s[1]-1] in ['-', 'L', 'F']: #Looking left of S
    c = (s[0], s[1]-1, 'l')

stp = 1
cListRow = [s[0], c[0]]
cListCol = [s[1], c[1]]
cList = [s, c[:2]]

while True:
    pipe = tb[c[0]][c[1]]
    if pipe == 'S':
        break
    shift = shiftDict[pipe][c[2]]
    c = (c[0]+shift[0], c[1]+shift[1], shift[2])
    stp += 1
    cListRow.append(c[0])
    cListCol.append(c[1])
    cList.append(c[:2])

#Problem 1 solution
print(stp//2)

shp = 'POLYGON ((' + ', '.join([str(x[1]) + ' ' + str(x[0]) for x in cList]) + '))'

shp = wkt.loads(shp).buffer(-.5, cap_style='square', join_style='mitre')

#Problem 2 solution
print(shp.area)

# plotPoly = gpd.GeoSeries(shp)

# plotPoly.plot()
# plt.show()