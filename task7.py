# import json
# import itertools
# with open("task5.json",'r') as p:
# 	data=json.load(p)
# 	all_lang_list=[]
# 	for k in data:
# 		for i,j in k.items():
# 			if "director" ==i:
# 				all_lang_list.append(j)
# 	single_list=list(itertools.chain(*all_lang_list))
# 	unique_lang_list=[]
# 	count=0
# 	for lk in single_list:
# 		if lk not in unique_lang_list:
# 			unique_lang_list.append(lk)
# 	for doop in unique_lang_list:
# 		count=0
# 		for single_lang_ in single_list:
# 			if doop==single_lang_:
# 				count+=1
# 		print(doop,":",count)



import json
with open("task5.json",'r') as p:
	data=json.load(p)
	all_lang_list=[]
	for k in data:
		for i,j in k.items():
			if "director"==i:
				all_lang_list.append(j)
	single_list=[]
	for one in all_lang_list:
		for two in one:
			single_list.append(two)
	all_single=[]
	for single_ in single_list:
		if single_ not in all_single:
			all_single.append(single_)
	for language in all_single:
		count=0
		for all_lang_ in single_list:
			if language==all_lang_:
				count+=1
		print(language,":",count)