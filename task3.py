import json,pprint
with open('task1.json','r') as p:

	data=json.load(p)
	round_=[]
	for i in data:
		if i["year"] not in round_:
			round_.append(i["year"])
	print(round_)
	list_of_decade_year=[]
	for k in round_:
		a=k%10
		b=k-a
		list_of_decade_year.append(b)
	print(list_of_decade_year)
	dummy=list(set(list_of_decade_year))
	d1=dummy.sort()
	dict1={}
	for doop in dummy:
		print(doop)
		sum2=doop+10
		lis=[]
		for dop in range(doop,sum2):
			for main in data:
				if dop == main["year"]:
					lis.append(main)
			dict1[doop]=lis
		pprint.pprint(dict1)







		
# import json,pprint
# with open('task1.json','r') as p:

# 	data=json.load(p)
# 	round_=[]
# 	for i in data:
# 		if i["year"] not in round_:
# 			round_.append(i["year"])
# 	print(round_)
# 	list_of_decade_year=[]
# 	for k in round_:
# 		a=k%10
# 		b=k-a
# 		list_of_decade_year.append(b)
# 	print(list_of_decade_year)
# 	dummy=list(set(list_of_decade_year))
# 	d1=dummy.sort()
# 	dict1={}
# 	for doop in dummy:
# 		lis=[]
# 		for dop in range(doop,doop+10):
# 			for main in data:
# 				if dop==main["year"]:
# 					lis.append(main)
# 		dict1[doop]=lis
# 	pprint.pprint(dict1)
	



	
