import random
import time
import math

# sequence form = 	1/0			read/write
#					user iD 	[1,20]
#					role		[1,5]
#					date
# 					time
# 					attribute number accessed
#
# total number of attributes = 15

MU = 13
SIGMA = 1.3  # visualization at https://homepage.stat.uiowa.edu/~mbognar/applets/normal.html


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.
    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval theo be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)


MIN = 9
MAX = 17


def randomTimeUniform():
    t = round(random.gauss(MU, SIGMA), 2)
    t_hr = math.floor(t)
    t_min = round((t - t_hr) * 60)
    return "{}:{:02d}".format(t_hr, t_min)


def randomTimeSkew(bias=11, influence=1):
    '''BIAS = 11
    INFLUENCE = 1  #between [0.0, 1.0]'''
    rnd = random.random() * (MAX - MIN) + MIN
    mix = random.random() * influence
    t = round(rnd * (1 - mix) + bias * mix, 2)
    t_hr = math.floor(t)
    t_min = round((t - t_hr) * 60)
    return "{}:{:02d}".format(t_hr, t_min)


# def randomTime(func):
# 	if func == 'uniform':
# 		return randomTimeUniform()
# 	elif func == 'skew':
# 		return randomTimeSkew()
# 	else:
# 		raise Exception

# print(randomDate("1/1/2018", "1/1/2019", random.random()))
# randomTime('skew')

def getTimeStamp(min_date, max_date, bias=11, influence=1):
    '''returns an array of random or biased timestamps of a specified size '''
    ts = randomDate(min_date, max_date, random.random()) + ' ' + randomTimeSkew(bias, influence)
    #	print(ts)
    return ts

    # getTimeStamp("1/1/2018", "1/1/2019")