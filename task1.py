import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup 

page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(page.text,"html.parser")

def scrap_top_list():
	main_div=soup.find("div",class_="lister")
	tbody=main_div.find("tbody",class_="lister-list")
	trs=tbody.find_all("tr")

	movie_ranks=[]
	movie_name=[]
	year_of_realease=[]
	movie_urls=[]
	movie_ratings=[]

	for tr in trs:
		position=tr.find("td",class_="titleColumn").text.strip().split()[0]
		# print(int(float(position)))          	  
		movie_ranks.append(int(float(position)))

		title=tr.find('td',class_="titleColumn").find('a').text
		movie_name.append(title)

		year=tr.find('td',class_="titleColumn").find('span').text
		year_of_realease.append(year)

		imdb_rating=tr.find('td',class_="ratingColumn imdbRating").text
		movie_ratings.append(imdb_rating)

		link=tr.find('td',class_="titleColumn").a["href"]
		movie_link="https://www.imdb.com"+link
		movie_urls.append(movie_link)

	Top_movies=[]
	details={'position':'','name':'','year':'','rating':'','url':''}
	for i in range(0,len(movie_name)):
		details["position"]=int(movie_ranks[i])
		details['name']=str(movie_name[i])
		details['year']=int(year_of_realease[i][1:5])
		details['rating']=float(movie_ratings[i])
		details['url']=movie_urls[i]
		Top_movies.append(details.copy())
	pprint(Top_movies)

	pprint(scrap_top_list)
	with open("task1.json",'w') as f:
		movies=scrap_top_list()
		json.dump(movies,f,indent=4)













