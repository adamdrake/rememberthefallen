import pandas as pd
import datetime
import sys
pd.options.mode.chained_assignment = None

data = pd.read_csv(sys.argv[1], sep='|', low_memory=False, header=None)
kia = data[(data[44] == 'KILLED IN ACTION')]
kia.rename(columns={7 : 'rank', 34 : 'dod', 35 : 'yod', 30 : 'countryOfDeath'}, inplace=True)

kia['dod'] = kia['dod'].astype(str)
kia['dodlen'] = kia['dod'].apply(lambda x: len(str(x)))
kia = kia[kia['dodlen'] == 8]

kia['name'] = kia[4].apply(lambda x: x.split(' ')[0] + ', ' + ' '.join(x.split(' ')[1:]))
kia['yod'] = kia['yod'].astype(str)

kia['dayDeath'] = kia['dod'].apply(lambda x: int(str(x)[6:]))
kia['monthDeath'] = kia['dod'].apply(lambda x: int(str(x)[4:6]))

kia['tweet'] = kia['rank'] + " " + kia['name'] + ", " + "KILLED IN ACTION, " + kia['countryOfDeath'] + ". " + "(" + kia['yod'] + ")"

toTweet = kia[['tweet', 'dayDeath', 'monthDeath']]
toTweet.to_csv('kia.tweets.dat', sep='|', index=False, headers=None)
