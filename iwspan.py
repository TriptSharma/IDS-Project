
#weight is a dictionary containing weights of all the items

threshold = 0.3

def is_subseq(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)

def wspan(sequences,weight):
	tsmw = 0
	smw = {}
	itemseq = {}
	for seq in sequences:
		maxweight = 0
		for item in seq:
			if item not in itemseq.keys():
				itemseq[item] = {}
				itemseq[item][seq] = 0
			elif seq not in itemseq[item].keys():
				itemseq[item][seq] = 0
			if weight[item]>maxweight:
				maxweight = weight[item]
		smw[seq] = maxweight
		tsmw = tsmw + maxweight


	# print(itemseq)
	# print(tsmw)

	itemswub = {}
	itemwsup = {}
	for item in itemseq.keys():
		totalsmw = 0
		totalwI = 0
		for seq in itemseq[item].keys():
			totalsmw = totalsmw + smw[seq]
			totalwI = totalwI + weight[item]
		itemswub[item] = totalsmw/tsmw 
		itemwsup[item] = totalwI/tsmw 

	# print(itemswub)
	# print(itemwsup)


	WFUB = []
	WS = []

	for item in itemswub.keys():
		if itemswub[item]>=threshold:
			WFUB.append(item)
		if itemwsup[item]>=threshold:
			WS.append(item)

	r = 1

	WFUB = sorted(WFUB)
	WS = sorted(WS)

	projSDB = {}

	# print (WFUB)
	# print (WS)

	for item in WFUB:
		for seq in sequences:
			projseq = ''
			counter = 0
			for i in seq:
				if i==item and counter==0:
					projseq = ''
					counter = 1
				if i in WFUB:
					projseq = projseq + i
			if len(projseq)>=r+1 and item in seq:
				if item not in projSDB.keys():
					projSDB[item] = {}
					projSDB[item][projseq] = 0
				else:
					projSDB[item][projseq] = 0
		if item=='D' or True:
			WS+=(find_ws(item,projSDB[item],r,weight,tsmw))

	return WS


def find_ws(x,sdbx,r,weight,tsmw):

	# print (x)
	# print (sdbx)

	ts = {}
	for seq in sdbx.keys():
		for i in range(r,len(seq)):
			toadd = x
			toadd += seq[i]
			if toadd not in ts:
				w = 0
				for j in toadd:
					w=w+weight[j]
				ts[toadd] = w/len(toadd)

	# print (ts)

	WFUB = []
	WS = []
	dic = {}
	for i in ts.keys():
		counter = 0
		for seq in sdbx.keys():
			if is_subseq(i,seq):
				counter += 1
		wsup = ts[i]*counter/tsmw
		if wsup>=threshold:
			WS.append(i)
		totalweight = 0
		for seq in sdbx.keys():
			if is_subseq(i,seq):
				maxweight = 0
				for k in seq:
					if weight[k]>maxweight:
						maxweight = weight[k]
				totalweight += maxweight
		swub = totalweight/tsmw
		dic[i] = [wsup,swub]
		if swub>=threshold:
			WFUB.append(i)

	# print(dic)

	PI = []
	for i in WFUB:
		for j in i:
			if j not in PI:
				PI.append(j)

	WFUB = sorted(WFUB)
	WS = sorted(WS)

	# print (WFUB)
	# print (WS)

	projSDB = {}
	WS1 = []

	for item in WFUB:
		for seq in sdbx.keys():
			projseq = ''
			counter = 0
			index = seq.find(item)
			if index!=-1:
				for u in range(index,len(seq)):
					if seq[u] in PI:
						projseq += seq[u]
			if len(projseq)>=r+1:
				if item not in projSDB.keys():
					projSDB[item] = {}
					projSDB[item][projseq] = 0
				else:
					projSDB[item][projseq] = 0
		if item in projSDB.keys():
			WS += (find_ws(item,projSDB[item],r+1,weight,tsmw))
	return WS


sequences = ['BCB','DECHF','ACFDEF','FGH','CDACEF']
wights = {'A':0.1,'B':0.15,'C':0.2,'D':0.3,'E':0.45,'F':0.55,'G':0.65,'H':0.95}
print(wspan(sequences,wights))










