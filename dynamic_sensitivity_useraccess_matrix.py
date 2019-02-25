def dynamic_sens(trans):
	count = {}
	for tran in trans:
		role = tran[1]
		atts = tran[3]
		if role in count.keys():
			for att in atts:
				if att in count[role].keys():
					count[role][att] += 1 
				else:
					count[role][att] = 1
		else:
			for att in atts:
				count[role][att] = 1

	dyn_sen = {}
	for i in count.keys():
		for j in count[i].keys():
			dyn_sen[i][j] = (1/count[i][j],ret_sens_mapping(count[i][j]))


	return dyn_sen



def user_access_matrix(trans):
	count = {}
	for tran in trans:
		user = tran[2]
		atts = tran[3]
		if user in count.keys():
			for att in atts:
				if att in count[user].keys():
					count[user][att] += 1 
				else:
					count[user][att] = 1
		else:
			for att in atts:
				count[user][att] = 1

	return count


def ret_sens_mapping(count):
	map = {x:'high',y:'moderate',z:'low'}
	if count<= :
		return map[z]
	elif count<= :
		return map[y]
	else:
		return map[x]
