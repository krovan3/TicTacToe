import random
a = 1
default_matrix = ['xd',"1","2","3","4","5","6","7","8","9"]


def tie_checker(matrix):
    super_default_matrix = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(super_default_matrix)):
        if super_default_matrix[i] not in matrix:
            pass
        else:
            return 0
    return 1


def to_win(pole):
        if pole[1] == pole[2] == pole[3]: return 1
        if pole[4] == pole[5] == pole[6]: return 1
        if pole[7] == pole[8] == pole[9]: return 1
        if pole[1] == pole[5] == pole[9]: return 1
        if pole[3] == pole[5] == pole[7]: return 1
        if pole[1] == pole[4] == pole[7]: return 1
        if pole[2] == pole[5] == pole[8]: return 1
        if pole[3] == pole[6] == pole[9]: return 1
        else:
            return 0


def spravka():
    print("Для хода введите число от 1 до 9 Вам необходимо составить 3 крестика (нолика) в ряд, чтобы победить")
    for i in range(1, 10):
        print(f'| {default_matrix[i]} |', end="")
        if i % 3 == 0:
            print("\n", end="")
            print("- - - - - - - -")


def hod(hod, game_matrix, sign):

    if hod in game_matrix:
        for i in range(10):
            if game_matrix[i] == hod:
                game_matrix[i] = sign
        for i in range(1, 10):
            print(f'| {game_matrix[i]} |', end="")
            if i % 3 == 0:
                print("\n", end="")
                print("- - - - - - - -")
        return 1
    else:
        print("Неправильный ход")
        for i in range(1, 10):
            print(f'| {default_matrix[i]} |', end="")
            if i % 3 == 0:
                print("\n", end="")
                print("- - - - - - - -")
        return 0


def game(name1,turn,game_matrix):
        bots_matrix = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        sign="✟"
        if turn==1:
           CurrentPlayer=name1
        else:
           CurrentPlayer="AI"
        while True:
            if CurrentPlayer == name1:
                print(f"Ход - {CurrentPlayer} {sign}")
                hod1 = (input())
                while hod(hod1,game_matrix,sign)==0:
                    print(f"Ход - {CurrentPlayer} {sign}")
                    hod1 = (input())
                bots_matrix.remove(hod1)
                if to_win(game_matrix):
                    print(f"{CurrentPlayer} win")
                    with open('results.txt', 'a') as f:
                        print(f'{name1} ai: {CurrentPlayer}', file=f)
                    break
                if tie_checker(game_matrix):
                    print("tie")
                    with open('results.txt', 'a') as f:
                        print(f'{name1} ai : tie', file=f)
                    break
                if CurrentPlayer==name1:
                    CurrentPlayer="ai"
                else:
                    CurrentPlayer=name1
                if sign=="✟":
                    sign="O"
                else:
                    sign="✟"
            else:
                sign = "O"
                hod1 = random.choice(bots_matrix)
                print(f"Я пошёл {hod1}: ")
                while hod(hod1, game_matrix, sign) == 0:
                    hod1 = random.choice(bots_matrix)
                bots_matrix.remove(hod1)
                if to_win(game_matrix):
                    print(f"{CurrentPlayer} win")
                    with open('results.txt', 'a') as f:
                        print(f'{name1} ai: {CurrentPlayer}', file=f)
                    break
                if tie_checker(game_matrix):
                    print("tie")
                    with open('results.txt', 'a') as f:
                        print(f'{name1} ai : tie', file=f)
                    break
                CurrentPlayer = name1
                sign = "✟"

while a:
    default_matrix = ['xd',"1","2","3","4","5","6","7","8","9"]
    print('Добро пожаловать в игру "Крестики-нолики"')
    print('Меню:')
    print('1. Новая игра')
    print('2. Просмотреть результаты')
    print('3. Справка')
    print('4. Выход')
    a = int(input())
    a = a - 4
    if a == -1:
        spravka()
    if a == -2:
        with open("results.txt", "r") as f:
            text=f.read()
            print(text)
    if a == -3:
        print("Введите имя первого игрока: ")
        name1 = (input())
        r = random.randint(1,2)
        if r % 2 == 0:
            turn = 1
        else:
            turn = 2
        game(name1,turn,default_matrix)