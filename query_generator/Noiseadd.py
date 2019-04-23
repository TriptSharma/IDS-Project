import random
import numpy as np
from getts import getTimeStamp
import pickle
import json

with open("settings.json") as ifile:
    settings = json.load(ifile)
#
# with open("pure_role_file.obj",'rb') as ifile:
#     data = pickle.load(ifile)

def inflatedata(dat,distribution,total):
    data = []
    for i,elem in enumerate(dat):
        data.append(np.tile(elem,(int(distribution[i]*total)+1,1)))
    return data

def getDistribution(unik):
    rands = []
    leng = len(unik)
    for elem in range(leng):
        rands.append(np.random.randint(10,60))
    rands.sort()
    temp_sum = sum(rands)
    rands = [(x/temp_sum) for x in rands]
    return rands

def masterNoise(sequence,elem):
    temp = list(set(sequence) - set(elem))
    to_select = len(elem)
    for i in range(to_select):
        temp.append(-1)
    random.shuffle(temp)
    selected = random.sample(temp, len(elem))
    trop = [None] * (len(elem) * 2)
    trop[::2] = elem
    trop[1::2] = selected
    trop = [x for x in trop if x != -1]
    return trop

def addNoise(total,data):
    mega_data = []
    for i,role in enumerate(data):
        all_q = []
        for j,user in enumerate(role):
            distr = getDistribution(user)
            data_inf = inflatedata(user,distr,total)
            accessible = settings['TABLE_ACCESS_PERMISSION'][i]
            attrib_list = []
            for tab in accessible:
                for i1 in range(settings['NO_ATTRIB_PER_TABLE'][tab]):
                    attrib_list.append(str(tab) + str(i1))
            bias = 13  # mean
            influence = 1  # deviation; value between [0,1)
            final1 = []
            for elem in data_inf:
                for row in elem:
                    final1 = []
                    final1.append(i)
                    final1.append(j)
                    final1.append(getTimeStamp("1/1/2018", "1/1/2019", bias, influence))
                    row = masterNoise(attrib_list,row)
                    final1.append(row)
                    all_q.append(final1)
        mega_data.append(all_q)
    return mega_data
