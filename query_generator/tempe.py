import random
import numpy as np
from getts import getTimeStamp

NO_USERS_PER_ROLE = 5
NO_ROLES = 5
NO_ATTRIBS = 15
NO_TABLES = 3
NO_TRANS_PER_USER = 100
COMMON_SEQ_LEN = 3
USER_SEQ_LEN = 3
NO_ROLE_SEQ = 4
NO_USER_SEQ = 3

sequence = np.arange(1,NO_ATTRIBS,1)

def addNoise(data,rang):
    distrib = getDistribution(rang)
    for i in range(len(distrib)):
        data.append(np.tile(get_rand_seq(), (distrib[i] *5, 1)))
    return(data)

def get_rand_seq():
    rw = np.random.randint(0,2)
    u1 = np.random.choice(sequence,np.random.randint(COMMON_SEQ_LEN,NO_ATTRIBS-COMMON_SEQ_LEN),False)
    if(rw%2==0):
        rw = np.random.randint(0, 2)
    u1 = np.insert(u1,0,rw)
    return u1

def get_seq(low,var,data=[]):
    times = np.random.randint(low, var)
    for x in range(times):
        data.append(get_rand_seq())
    return data

def inflatedata(dat,distribution):
    data = []
    for i,elem in enumerate(dat):
        data.append(np.tile(elem,(distribution[i]*10,1)))
    return data

def getDistribution(unik):
    rands = []
    for elem in range(len(unik)):
        rands.append(np.random.randint(0,100-len(unik)))
    rands.sort()
    last = rands[0]
    for i in range(1,len(rands)):
        temp = rands[i]
        rands[i] = temp-last
        last = temp
    rands.append(100 - temp)
    rands.sort(reverse=True)
    return rands

def masterNoise(elem):
        temp = list(set(sequence.flat)-set(elem.flat))
        to_select = len(elem)
        for i in range(to_select):
            temp.append(-1)
        random.shuffle(temp)
        selected = random.sample(temp,len(elem))
        trop = [None]*(len(elem)*2)
        trop[::2] = elem
        trop[1::2]= selected
        trop = [x for x in trop if x!=-1]
        return trop

if __name__ == "__main__":
    all_q = []
    for rid in range(NO_ROLES):
        rolseq = get_seq(2,NO_ROLE_SEQ)
        for uid in range(NO_USERS_PER_ROLE):
            usrtmp = rolseq
            usrtmp = get_seq(1,NO_USER_SEQ,usrtmp)
            distr = getDistribution(usrtmp)
            dat = inflatedata(usrtmp,distr)
            dat = addNoise(dat,usrtmp)
            final = []
            bias = 13   #mean
            influence = 1   #deviation; value between [0,1)
            for elem in dat:
                for ele in elem:
                    final.append(uid)
                    final.append(getTimeStamp("1/1/2018", "1/1/2019", bias, influence))
                    final.append(rid)
                    ele = masterNoise(ele)
                    final.append(ele)
                    #print(ele, final, '\n')
                    all_q.append(final)
                    # print(final)
                    final=[]

    for elem in all_q:
        print(elem)