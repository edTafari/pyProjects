def hangman(word):
    count = 0
    stages = ["",
              "-----------          ",
              "|         |          ",
              "|         |          ",
              "|         0           ",
              "|       / | \        ",
              "|        / \         ",
              "|                    "
              ]
    rletters = list(word)
    board = ["-"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    while count < len(stages) - 1:
        print("\n")
        message = "Введите букву: "
        char = input(message)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            count += 1
        print((" ".join(board)))
        e = count + 1
        print("\n".join(stages[0: e]))
        if "-" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: count]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))
hangman("Кот")