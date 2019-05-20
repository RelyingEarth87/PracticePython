def main():
    import datetime
    inp  = input("Enter your name and age, separated by a comma. ")

    d = datetime.datetime.today()
    yr = d.year
    inp1 = inp.split(",")
    name = inp1[0]
    age = inp1[1]
    age = age.replace(" ", "")
    age = int(age)

    birthyear = yr - age

    hundo = birthyear + 100

    print("{0}, you will turn 100 in the year {1}.".format(name, hundo))
    
main()
