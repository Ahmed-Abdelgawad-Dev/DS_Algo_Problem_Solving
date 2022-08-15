for line in range(int(input())):
    word = input()
    if len(word) > 10:
        print(str(word[0]) + str(len(word[1:-1])) + str(word[-1]))
    if len(word) <= 10:
        print(word)