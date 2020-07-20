import requests
import time
import json,string,pprint
from bs4 import BeautifulSoup 
all_links=[]
with open("task1.json",'r') as p:
	data=json.load(p)
	for i in data:
		all_links.append(i["url"])
user =int(input("enter how many movies you want"))
# length=user-1
all_lists=[]

for link in range(user):
	page=requests.get(all_links[link])
	# help(time(5).sleep)
	soup=BeautifulSoup(page.text,"html.parser")

	main_div=soup.find("div", class_="titleBar")

	name_of_m=''
	runtime_time=''
	name_director=[]
	type_of_movie=[]
	name_of_country=''
	name_of_language_=[]
	movies={}
	name1=main_div.find("h1").text

	for i in name1:
		if i=="\xa0":
			break
		else:
			name_of_m+=i

	year1=main_div.find("a").text
	year_of_m=int(year1)




	main_div2=soup.find("div",class_="plot_summary")
	movie_bio=main_div2.find("div",class_="summary_text").text.strip()


	main_div3=soup.find("div",class_="credit_summary_item")
	director=main_div3.find_all("a")
	for direct in director:
		name_director.append(direct.text)

	main_div4=soup.find("div",class_="subtext")
	typ_=main_div4.find_all("a")
	for gener in typ_:
		type_of_movie.append(gener.text)

	main_div5=soup.find_all("div",class_="txt-block")
	for i in main_div5:
		if "Country" in i.text:
			country_=i.find("a").text
		elif "Language" in i.text:
			Language_=i.find_all("a")
			for j in Language_:
				name_of_language_.append(j.text)
		elif "Runtime" in i.text:
			runtime_m=i.find_all("time")
			for ti in runtime_m:
				runtime_time=(ti.text)
	main_div6=soup.find("div",class_="poster").img["src"]
	movies["name"]=name_of_m
	movies["year"]=year_of_m
	movies["time"]=runtime_time
	movies["bio"]=movie_bio
	movies["director"]=name_director
	movies["gener"]=type_of_movie
	movies["language"]=name_of_language_
	movies["country"]=country_
	movies["link"]=main_div6
	# print(movies)
	all_lists.append(movies)
pprint.pprint(all_lists)
# with open("task5.json",'w') as p:
# 	data=json.dump(all_lists,p, indent=4)


	# movie_single()
	# all_lists.append(movie_single())
	# pprint.pprint(all_lists)





