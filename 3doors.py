#change or not
import random

change = True
#change = False

times = 10;
count = 0;
for i in range (times):
    D = ['d1','d2','d3','d4','d5''d6','d7''d8','d9','d10'];
    D = ['d1','d2','d3']
    car = random.sample(D,1)[0];
    first_choose = random.sample(D,1)[0];
    #print(car,first_choose)
    if first_choose == car:
        D.remove(car)
        lefted = random.sample(D,1)[0];
    else:
        lefted = car;
        
    if change:
        last_choose = lefted;
    else:
        last_choose = first_choose;
        
    if last_choose == car:
        count = count + 1;

print('if change, correct ',str(count) + ' times in ' + str(times));

##########################################################################################

import pandas_datareader.data as web
import datetime

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 1, 27)
#f = web.DataReader('GOOG', 'google', start, end)
#print(f)

##########################################################################################

c = list(range(1, 41))
p = list(range(1, 21))
#print(c)
#print(p)
print(random.sample(c, 6),random.sample(p, 1))



##########################################################################################

import sklearn