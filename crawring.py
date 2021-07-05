import requests
from bs4 import BeautifulSoup
import re

# 1. naver 영화 url 가져오기
def get_movie_link(url):

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html5lib')
    movie_links = soup.select('a[href]')

    movie_links_list = []

    for link in movie_links:
        if re.search(r'st=mcode&sword' and r'&target=after', link['href']):
            target_url = r'http://movie.naver.com/movie/point/af/list.nhn'+str(link['href'])
            movie_links_list.append(target_url)
            print(target_url)


    return movie_links_list

url = 'http://movie.naver.com/movie/point/af/list.nhn'
movie_links = get_movie_link(url)
print(movie_links)

# 2. 영화 접속후 
res = requests.get('https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=189050&target=after')

def genre_link(url):
    movie_links_list = get_movie_link(url)
    genre_list=[]

    for movie_url in movie_links_list:
        res = requests.get(movie_url)
        content = res.text
        soup = BeautifulSoup(content, 'html5lib')
        genre = soup.find_all('table',class_='info_area')

        for genre in genre:
            genre_list.append(genre.a.get_text())

    return genre_list

url = 'http://movie.naver.com/movie/point/af/list.nhn'
genre_link_data = genre_link(url)
# print(genre_link_data)

## naver 영화에서 평가등을 한 유저 정보 가져오기
def get_user_list(url):
    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, 'html5lib') #?

    page_links = soup.select('a[href]')
    page_link_list = []

    for link in page_links:
        if re.search(r'st=mcode&sword' and r'&target=after', link['href']):
            target_url='http://movie.naver.com'+str(link['href'])
            page_link_list.append(target_url)

    # 이게 뭘 처리하는건가?
    if len(page_link_list) !=1 :
        pop_number = len(page_link_list) - 1
        page_link_list.pop(pop_number)

    return page_link_list

# url = "http://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=189120&target=after&page=1"
# point_data = get_user_list(url)
# print(point_data)