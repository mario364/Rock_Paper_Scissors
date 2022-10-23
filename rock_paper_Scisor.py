import random
import time

machine_answres = ["Камень", "Ножницы", "Бумага"]


def play():
    while True:
        player_answer = input('Камень, Ножницы, Бумага? ')
        machine_answres1 = random.choice(machine_answres)
        print(f'Ответ игрока: {player_answer}')
        time.sleep(1)
        print(f'Ответ машины: {machine_answres1}')
        time.sleep(1)
        if player_answer == "Камень" and machine_answres1 == 'Ножницы' or player_answer == "Ножницы" and machine_answres1 == 'Бумага' or player_answer == 'Бумага' and machine_answres1 == "Камень":
            time.sleep(1)
            print('Ты победил! Дай пять!')
        elif player_answer == machine_answres1:
            time.sleep(1)
            print("Ничья")
        else:
            time.sleep(1)
            print("Ты проиграл! Утешительное дай пять!")
        new_game = int(input('Хочешь сыграть еще раз?\n1 - Еще раз\n2 - Выйти '))
        if new_game == 1:
            print("Сыграем еще раз!")
            continue
        if new_game == 2:
            print('Значит в следующий раз! Пока!')
            break

print('Привет! Давай сыграем в камень, ножницы бумага!')
play()
