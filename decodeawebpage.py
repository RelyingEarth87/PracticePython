def main():
    import requests
    from bs4 import BeautifulSoup

    site = 'https://www.nytimes.com/'
    r = requests.get(site)
    soup = BeautifulSoup(r.text, features='lxml')

    headlines = soup.find_all('h2', class_='css-1qwxefa esl82me0')

    print("The headlines from the New York Times are: ")

    for i in headlines:
        i = i.prettify()
        s = i.split(">")
        head = s[2]
        head = head.split("<")
        print(head[0])



main()
