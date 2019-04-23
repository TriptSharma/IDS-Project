from master import pure_queries
from Noiseadd import addNoise
import pickle

pure = pure_queries()
final_data = addNoise(1000,pure)

with open("simulated_queries.obj","wb+") as ofile:
    pickle.dump(final_data,ofile)

'''
format for each entry in the data:
1st -> role_id
2nd -> user_id
3rd -> time_stamp
4th -> query (1st number signifies whether its an read or write (old rule))
the 1000 argument in the above roll gives 1000 queries for each user
'''