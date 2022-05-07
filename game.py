elements = ['○','○','○','○',' ','●','●','●','●']
win = elements.copy()
win.reverse()
shet = 1
best = 0
game = 0
retry = 0

print ("Игра 'Кружочки'. Ваша задача поменять кружочки местами, делая перемещения в пустые места, но не более чем через один кружочек")
while game != 1:
    while elements != win:
        if retry == 1:
            print('\nYou win!\nYou score:', shet)
            if best == 0:
                best = shet
            elif shet < best:
                best = shet                
            print("You best score:", best)
            retr = str(input("Хочешь попробывать снова? (Y/N) "))
            if retr == "Y":
                shet = 1
                retry -= 1
                continue
            else:
                game += 1
                break
        else:
            print ("\nДля выхода из игры введите '111'")
            print ("Чтобы начать заного введите '222'\n")
            for i in range(9):
                print(elements[i], end=' ')
            print()
            for i in range(9):
                print(i, end=' ')
            print() 
            print ("Ход", shet)
            first = int(input("Что переместить (цифра) -> "))
            if first == 111:
                game += 1
                break
            elif first == 222:
                elements = ['○',' ','●']
                shet = 1
                continue
            else:
                second = int(input("Куда переместить (цифра) -> "))
            if second == 111:
                game += 1
                break
            elif second == 222:
                elements = ['○',' ','●']
                shet = 1
                continue
            elif first > second:
                maxi = first
                mini = second
            else:
                maxi = second
                mini = first
            if maxi - mini <= 2 and elements[second] == ' ':
                elements[second] = elements[first]
                elements[first] = ' '
                shet += 1
            else:
                print('\n!!!Невозможная комбинация!!!')            
        if elements == win:
            print()
            for i in range(9):
                print(elements[i], end=' ')
            print()
            for i in range(9):
                print(i, end=' ')
            print()
            elements = ['○',' ','●']
            shet -= 1
            retry += 1
            continue
        
