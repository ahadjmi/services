from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/"

def main(n):
    k_base={}
    data_base = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    print(soup)

    for name in soup.find_all('td',class_='titleColumn',limit=n):
        movie_name = name.a.text
        cast = name.a['title'].split(", ")
        for actor in cast:
            data_base.setdefault(actor, []).append(movie_name)
        k_base[movie_name]=cast
        print(movie_name)
        #print(cast)
    print(data_base)
    return data_base
    #print(k_base)
    #print(soup.prettify())

if __name__ == '__main__':
    n=int(input("N is: "))
    data_base=main(n)
    actor = input("Enter actor name: ")

    if data_base[actor]:

        for movie in data_base[actor]:
            print(movie)