import pandas as pd 
from collections import Counter

def handType(dict):
    hand = sorted(list(dict.values()), reverse=True)
    if hand[0] == 5:
        return 6
    elif hand[0] == 4:
        return 5
    elif hand[0] == 3 and hand[1] == 2:
        return 4
    elif hand[0] == 3 and hand[1] == 1:
        return 3
    elif hand[0] == 2 and hand[1] == 2:
        return 2
    elif hand[0] == 2 and hand[1] == 1:
        return 1
    elif len(hand) == 5:
        return 0
    else:
        return -1
    
def handTypeJoker(dict):
    if 'J' in dict and dict['J'] != 5:
        jVal = dict['J']
        dict = {k:v for (k,v) in dict.items() if 'J' not in k}

        maxVal = max(dict.values())
        maxKey = list({k:v for (k,v) in dict.items() if maxVal == v})[0]

        dict[maxKey] = dict[maxKey] + jVal

    return handType(dict)

    

cardStr = {'A': 'A',
           'K': 'B',
           'Q': 'C',
           'J': 'D',
           'T': 'E',
           '9': 'F',
           '8': 'G',
           '7': 'H',
           '6': 'I',
           '5': 'J',
           '4': 'K',
           '3': 'L',
           '2': 'M'}

df = pd.read_csv('T:/SideProjects/AdventOfCode/2023-07/Input.csv', delim_whitespace=True, names=['Hand', 'Bet'])

df['HandType'] = df.Hand.apply(lambda x: handType(Counter(x)))
df['HandUpdate'] = df.Hand.replace(to_replace=cardStr, regex=True)
df = df.sort_values(by=['HandType', 'HandUpdate'], ascending=[False, True])
df['Rank'] = range(len(df), 0, -1)
df['NewBet'] = df.Bet * df.Rank

#Problem 1 solution
print(df.NewBet.sum())

df = df[['Hand', 'Bet']] #drop calculated columns
cardStr['J'] = 'N' #J is now weakest

df['HandType'] = df.Hand.apply(lambda x: handTypeJoker(Counter(x)))
df['HandUpdate'] = df.Hand.replace(to_replace=cardStr, regex=True)
df = df.sort_values(by=['HandType', 'HandUpdate'], ascending=[False, True])
df['Rank'] = range(len(df), 0, -1)
df['NewBet'] = df.Bet * df.Rank

print(df.NewBet.sum())

