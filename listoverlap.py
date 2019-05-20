def main():
    from random import randrange
    a_num = randrange(4, 15)
    b_num = randrange(4, 15)

    a = []
    b = []
    
    for i in range(a_num):
        x = randrange(1, 100)
        a.append(x)

    for i in range(b_num):
        x = randrange(1, 100)
        b.append(x)

    a.sort()
    b.sort()

    print(a, b)

    a = list(dict.fromkeys(a))
    b = list(dict.fromkeys(b))
        
    c = []

    for i in b:
        if i in a:
            c.append(i)

    print("The numbers that overlap in the two lists are:", c)

    



main()
