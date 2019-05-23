def main():
    it = int(input("How many Fibonnacci numbers would you like to see? "))

    seq = fib(it)

    print(seq)


def fib(it):
    fib_base = 1
    fib_seq = 0
    seq = [1]
    for i in range(0, it - 1):
        fib_base = fib_base + fib_seq
        seq.append(fib_base)
        fib_seq = seq[i]

    return seq

main()
