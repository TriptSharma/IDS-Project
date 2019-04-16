import numpy as np
from math import *

def get_time_dist(ts,x, sf=48, d=48):
	m = 24-ts
	inter = (x+m)/d
	inter2 = sf * abs(log10((inter/(1-inter))))
	return (1-min(1.0, sqrt(1/floor(inter2))))

print(get_time_dist(12, 10))
