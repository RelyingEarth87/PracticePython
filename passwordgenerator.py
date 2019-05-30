def main():
    strength = int(input("What strength would you like the password to be? (0 = weak, 1 = medium, 2 = strong) "))

    if strength == 0:
        x = password(0)
    elif strength == 1:
        x = password(1)
    elif strength == 2:
        x = password(2)
    elif strength > 2:
        x = password(2) + password(1)

    x = shuffle_word(x)

    print("Password =", x)


def password(strength):
    from random import randrange, random
    char = "abcdefghijklmnopqrstuvwxyz0123456789?!@#$%&*+=-_"
    pw = []

    if strength == 0:
        for i in range(8):
            num = randrange(0, 26)
            pw.append(char[num])

        word = pw[0] + pw[1] + pw[2] + pw[3] + pw[4] + pw[5] + pw[6] + pw[7]
    elif strength == 1:
        for i in range(12):
            num = randrange(0, 47)
            pw.append(char[num])

        word = pw[0] + pw[1] + pw[2] + pw[3] + pw[4] + pw[5] + pw[6] + pw[7] + pw[8] + pw[9] + pw[10] + pw[11]
    elif strength == 2:
        num = randrange(0, 26)
        a = char[num]
        a = a.upper()
        pw.append(a)
        for i in range(13):
            num = randrange(0, 47)
            pw.append(char[num])

        for i in range(len(pw)):
            if pw[i].isalpha():
                r = random()
                if r > .65:
                    pw[i] = pw[i].upper()

        word = pw[0] + pw[1] + pw[2] + pw[3] + pw[4] + pw[5] + pw[6] + pw[7] + pw[8] + pw[9] + pw[10] + pw[11] + pw[12] + pw[13]

    return word


def shuffle_word(word):
    from random import shuffle
    word = list(word)
    shuffle(word)

    return ''.join(word)


main()
