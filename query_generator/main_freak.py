from master import pure_queries
from Noiseadd import addNoise
import pickle
import os

def dumpQueries(path,num):
    pure = pure_queries()
    final_data = addNoise(num,pure)
    with open(path+"/simulated_queries.obj","wb+") as ofile:
        pickle.dump(final_data,ofile)

def makeFolders():
    queries = [1000,2000,3000,4000,5000] #these are queries per user for each role
    for elem in queries:
        print(os.getcwd())
        os.system("mkdir "+str(elem))
        dumpQueries(str(elem),elem)


if __name__ == '__main__':
    makeFolders()
'''
format for each entry in the data:
1st -> role_id
2nd -> user_id
3rd -> time_stamp
4th -> query (1st number signifies whether its an read or write (old rule))
the 1000 argument in the above roll gives 1000 queries for each user
'''