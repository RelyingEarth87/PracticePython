def main():
    import requests
    from bs4 import BeautifulSoup

    s = []
    t = []

    site = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    r = requests.get(site)
    soup = BeautifulSoup(r.text, features='lxml')

    title = soup.find_all('h1', class_='hed')

    a = str(title[0])
    b = a.split(">")
    c = b[1]
    d = c.split("<")
    e = d[0]

    print(e)

    article = soup.find_all('p')
    
    for i in article:
        i = i.prettify()
        s = i.split(">")
        t.append(s[1])

    for i in t:
        u = i.split("<")
        print(u[0])



main()
