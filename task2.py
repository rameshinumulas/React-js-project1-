import json,pprint
with open('task1.json','r') as p:
	list_of_year=[]

	data=json.load(p)
	for i in data:
		list_of_year.append(i["year"])
	print(set(list_of_year))
	dict1={}
	for doop in list_of_year:
		lis=[]
		for k in data:
			if doop==k["year"]:
				lis.append(k)

		dict1[doop]=lis
	pprint.pprint(dict1)




# import json
# from pprint import pprint
# with open('task1.json','r') as p:
# 	list_of_year=set()
# 	data=json.load(p)
# 	dic={}
# 	for i in data:
# 		lis=[]
# 		for j in data:
# 			if i["year"]==j["year"]:
# 				lis.append(j)
# 		dic[i["year"]] = lis
# 	pprint(dic)














import requests
import json,string,pprint
from bs4 import BeautifulSoup 


all_links=["https://www.imdb.com/title/tt0066763/"]
for i in range(len(user)):
	page=requests.get(all_links[i])
	soup=BeautifulSoup(page.text,"html.parser")

	def movie_single():
		main_div=soup.find("div", class_="titleBar")

		name_of_m=''
		runtime_time=''
		name_director=[]
		type_of_movie=[]
		name_of_country=''
		name_of_language_=[]
		name1=main_div.find("h1").text

		for i in name1:
			if i=="\xa0":
				break
			else:
				name_of_m+=i

		year1=main_div.find("a").text
		year_of_m=int(year1)

		main_div2=soup.find("div",class_="plot_summary")
		movie_bio=main_div2.find("div",class_="summary_text").text


		main_div3=soup.find("div",class_="credit_summary_item")
		director=main_div3.find("a").text
		name_director.append(director)

		main_div4=soup.find("div",class_="subtext")
		typ_=main_div4.find("a").text
		type_of_movie.append(typ_)

		main_div5=soup.find_all("div",class_="txt-block")
		for i in main_div5:
			if "Country" in i.text:
				country_=i.find("a").text
			elif "Language" in i.text:
				Language_=i.find("a").text
				name_of_language_.append(Language_)
			elif "Runtime" in i.text:
				runtime_m=i.find_all("time")
				for ti in runtime_m:
					runtime_time=(ti.text)

		main_div6=soup.find("div",class_="poster").img["src"]

		movies={}

		movies["name"]=name_of_m
		movies["year"]=year_of_m
		movies["time"]=runtime_time
		movies["bio"]=movie_bio
		movies["director"]=name_director
		movies["gener"]=type_of_movie
		movies["language"]=name_of_language_
		movies["country"]=country_
		movies["link"]=main_div6

		return movies

pprint.pprint(movie_single())

