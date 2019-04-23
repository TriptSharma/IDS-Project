import numpy as np
import time
import configparser
from getts import getTimeStamp
import json
import pickle
with open("settings.json") as ifile:
    settings = json.load(ifile)
def get_rand_seq(sequence,leng):
    rw = np.random.randint(0,2)
    u1 = np.random.choice(sequence,np.random.randint(4,leng),False)
    if(rw%2==0):
        rw = np.random.randint(0, 2)
    u1 = np.insert(u1,0,rw)
    return u1

def pure_queries():
    mega_roles = []
    for role in range(settings["NO_ROLES"]):
        accessible = settings['TABLE_ACCESS_PERMISSION'][role]
        attrib_list = []
        for tab in accessible:
            for i in range(settings['NO_ATTRIB_PER_TABLE'][tab]):
                attrib_list.append(str(tab)+str(i))
        collect = []
        for _ in range(settings['NO_TRANSACTION_PER_ROLE'][role]):
            collect.append(get_rand_seq(attrib_list,settings['ROLE_SEQ_LEN'][role]))

        num = 0
        rolez = []
        for num,i in enumerate(settings['NO_TRANSACTION_PER_USER'][role]):
            temp = []
            for seq in range(i):
                temp.append(get_rand_seq(attrib_list,settings['USER_SEQ_LEN'][role][num]))
            for elem in collect:
                temp.append(elem)
            rolez.append(temp)
        mega_roles.append(rolez)
    return mega_roles

if __name__ == "__main__":
    pure_queries()
