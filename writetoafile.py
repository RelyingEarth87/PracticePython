def main():
    import requests
    from bs4 import BeautifulSoup

    title = input("What would you like the name of the file to write New York Times headlines to be called? ")

    site = 'https://www.nytimes.com/'
    r = requests.get(site)
    soup = BeautifulSoup(r.text, features='lxml')

    headlines = soup.find_all('h2', class_='css-1qwxefa esl82me0')

    text = []

    for i in headlines:
        i = i.prettify()
        s = i.split(">")
        head = s[2]
        head = head.split("<")
        text.append(head[0])

    file = open(title, 'w')

    file.write("The headlines from the New York Times are: ")

    for i in text:
        file.write(i)
        

    



main()
