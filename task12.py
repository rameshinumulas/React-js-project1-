import requests,pprint,json
from bs4 import BeautifulSoup

				######################### for one movie ########################################



page =requests.get("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast")
soup= BeautifulSoup(page.text,"html.parser")

main_div=soup.find("div",class_="redesign")
table_text=main_div.find("table",class_="cast_list")
trs_list=table_text.find_all("tr",class_="even")
odd_list=table_text.find_all("tr",class_="odd")
all_data=trs_list
count_for_tr=0
all_name_list=[]
all_i_d_list=[]




for j in odd_list:
	a_ = j.find("td",class_="primary_photo")
	aie=a_.find("a")["href"][6:15]
	all_i_d_list.append(aie)
	name=a_.find("img")["alt"]
	all_name_list.append(name)
for i in trs_list:
	a_tag = i.find("td",class_="primary_photo")
	aies=a_tag.find("a")["href"][6:15]
	all_i_d_list.append(aies)
	names=a_tag.find("img")["alt"]
	all_name_list.append(names)
all_list=[]
for i in range(len(all_name_list)):
	all_dict={}
	all_dict["name"] = all_name_list[i]
	all_dict["id"] = all_i_d_list[i]
	all_list.append(all_dict)
pprint.pprint(all_list)


############################################## for all movie ####################


all_links=[]
with open("task1.json",'r') as p:
	data=json.load(p)
	for i in data:
		all_links.append(i["url"]+''+"fullcredits?ref_=tt_cl_sm#cast")
user =int(input("enter how many movies you want"))
count=1
for link in range(user):
	page=requests.get(all_links[link])
	soup= BeautifulSoup(page.text,"html.parser")

	main_div=soup.find("div",class_="redesign")
	table_text=main_div.find("table",class_="cast_list")
	trs_list=table_text.find_all("tr",class_="even")
	odd_list=table_text.find_all("tr",class_="odd")
	all_data=trs_list
	count_for_tr=0
	all_name_list=[]
	all_i_d_list=[]


	for j in odd_list:
		a_ = j.find("td",class_="primary_photo")
		aie=a_.find("a")["href"][6:15]
		all_i_d_list.append(aie)
		name=a_.find("img")["alt"]
		all_name_list.append(name)
	for i in trs_list:
		a_tag = i.find("td",class_="primary_photo")
		aies=a_tag.find("a")["href"][6:15]
		all_i_d_list.append(aies)
		names=a_tag.find("img")["alt"]
		all_name_list.append(names)

	all_list=[]
	all_cast={}
	for i in range(len(all_name_list)):
		all_dict={}
		all_dict["name"] = all_name_list[i]
		all_dict["id"] = all_i_d_list[i]
		all_list.append(all_dict )
	all_cast["cast"]=all_list
	pprint.pprint(all_cast)


# 	print(count)
# 	count+=1
# 	with open("task12.json","w") as p:
# 		json.dump(all_cast,p,indent=4)






# import webbrowser
# webbrowser.open('http://net-informations.com')








# import webbrowser
# all_language=[]
# language_link=[]
# page=requests.get("https://www.w3schools.com/default.asp")
# soup=BeautifulSoup(page.text,"html.parser")


# main_div=soup.find_all("div",class_="w3-col l6 w3-center")
# for k in main_div:
# 	link2=k.find("a")["href"]
# 	name2=k.find("a").text
# 	all_language.append(name2)
# 	language_link.append(link2)




# main_div2=soup.find("div",class_="w3-row w3-dark-grey w3-padding-32")
# all_div=main_div2.find_all("div",class_="w3-col l6 w3-center")
# # print(all)
# for i in all_div:
# 	link3=i.find("a")["href"]
# 	name3=i.find("a").text
# 	all_language.append(name3)
# 	language_link.append(link3)



# index=1
# for j in all_language:
# 	print(index,j)
# 	index+=1
# user=int(input("enter which language you want, enter that number:-"))
# print(all_language[user-1])

# for lin in language_link:
# 	webbrowser.open("https://www.w3schools.com/"+language_link[user-1])
# 	break









# page=requests.get("https://www.tutoria/home/navgurukul/Desktop/scraping/task12.json  lspoint.com/javascript/index.htm")
# soup=BeautifulSoup(page.text,"html.parser")

# main_div=soup.find_all("ul",class_="toc chapters")

# count=1
# for i in main_div:
# 	count+=1
# 	if count>2:
# 		# main_div2=i.find("li", class_="heading")
# 		a_tag=i.find("a")["href"]
# 		# a_tag_text=main_div2.find("a").text
# 		print(a_tag)
# 	# print(a_tag_text)
	# break

