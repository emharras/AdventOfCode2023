import pandas as pd

def prediction(seq):
    predSeq = []

    while True:
        predSeq.append(seq[-1])
        newSeq = []
        for i in range(len(seq)-1):
            newSeq.append(seq[i+1] - seq[i])

        if newSeq == [0 for x in range(len(newSeq))]:
            break 
        else:
            seq = newSeq

    return sum(predSeq)


df = pd.read_csv('T:/SideProjects/AdventOfCode/2023-09/Input.csv', names=['Seq'])

df['SeqList'] = df.Seq.str.split().apply(lambda x: [int(y) for y in x])

df['Prediction'] = df.SeqList.apply(prediction)

#Problem 1 solution
print(df.Prediction.sum())

df['SeqList'] = df.SeqList.apply(lambda x: x[::-1])

df['Prediction'] = df.SeqList.apply(prediction)

#Problem 2 solution
print(df.Prediction.sum())
    