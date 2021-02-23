import pandas as pd

#reading in the dictionary and training data set and retrieving comment that are longer than 0 characters
dict = pd.read_excel("Copy of sentimentanalysisdictionary.xlsx")
train = pd.read_csv('trainingdata.csv')

#segmenting the dictionary into change and no change
change = dict.iloc[:,0]
no_change = dict.iloc[:,1]

#retrieving comment and pattern number
comment = train.iloc[:,2]
pat_num = train.iloc[:,1]

#sentiment value
sent_val = list()

#iterating through each comment and retrieving each comment's value
for com in comment:
    com = str(com)
    num = 0
    for string in com.split():
        for c in change:
            c = str(c)
            if(string in c):
                num = num + 1
        for nc in no_change:
            nc = str(nc)
            if (string in nc):
                num = num - 1
    sent_val.append(num)

def avg(lst):
    return sum(lst)/len(lst)

def sd(lst):
    var = sum([((x - avg(lst)) ** 2) for x in lst]) / len(lst)
    res = var ** 0.5
    return res

tot_avg = avg(sent_val)
standard_dev = sd(sent_val)

#adding the sentiment values for each row into a dataframe with the pattern number and comment value
sent_val_series = pd.Series(sent_val)
sent_val_sd = ([((x - tot_avg)/standard_dev) for x in sent_val])
sent_val_sd_series = pd.Series(sent_val_sd)
df = pd.DataFrame({"Pattern Number": pat_num,
                   "Sentiment Value": sent_val_series,
                   "Sentiment Value Standard Deviation": sent_val_sd_series})

#grouping the sums of each comment values by pattern number
df_group = df.groupby(["Pattern Number"]).mean()

#adding score to grouped patterns
score = list()
for sd in df_group["Sentiment Value Standard Deviation"]:
    if (sd <= 0):
        score.append(0)
    elif (sd >= 2):
        score.append(20)
    else:
        score.append(10*sd)

df_group["Score"] = score
#writing out to csv
df_group.to_csv('ahold_scoring.csv')
