from random import randint

lowDigit   = 10     # low digit
highDigit  = 50     # high digit
digit      = 0      # digit
countInput = 0      # количество попыток угадать
win        = False  # угадал?
playGame   = True   # продолжается ли игра?
x          = 0      # число, которое вводит игрок
startScore = 100    # начальное количество очков
score      = 0      # текущее количество очков
maxScore   = 0      # максимальное количество очков за сессию

while playGame:
    digit = randint(lowDigit, highDigit)
    #print(f"number guessing", digit)
    print("-" * 30)
    coutInput = 0
    score = startScore
    print("компютер загодал число, попробуй отгадать!")

    while not win and score > 0:
        print("-" * 30)
        print(f"Заработанно очков: {score}")
        print(f"Рекорд: {maxScore}")
        x = ""

        while not x.isdigit():
            x = input(f"Введите число от {lowDigit} до {highDigit}: ")
            if not x.isdigit():
                print('.' * 27 + "Введите, пожалуйста, число.")

        x = int(x)

        if x == digit:
            win = True
        else:
            length = abs(x - digit)

            if length < 3:
                print("Очень горячо!")
            elif length < 5:
                print("Горячо!")
            elif length < 10:
                print("Тепло")
            elif length < 15:
                print("Прохладно")
            elif length < 20:
                print("Холодно")
            else:
                print("Ледяной ветер")

            if coutInput == 7:
                score -= 10

                if digit % 2 == 0:
                    print("Число чётное")
                else:
                    print("Число нечётное")
            elif countInput == 6:
                score -= 8

                if digit % 3 == 0:
                    print("Число делится на 3")
                else:
                    print("Число не делится на 3")
            elif countInput == 5:
                score -= 4

                if digit % 4 == 0:
                    print("Число делится на 4")
                else:
                    print("Число не делится на 4")
            elif coutInput > 2 and coutInput < 5:
                score -= 2

                if x > digit:
                    print("Загаданное число МЕНЬШЕ вашего")
                else:
                    print("Загаданное число БОЛЬШЕ вашего")

            score -= 5
        countInput += 1

    print('*' * 40)

    if x == digit:
        print("Победа! Поздравляем!")
    else:
        print("Ой, у вас закончились очки. Вы проиграли :(")

    if input("Enter - сыгратьущё, 0 - выход ") == "0":
        playGame = False
    else:
        win = False

    if score > maxScore:
        maxScore = score

print('*' * 40)
print("""Спасибо что сыграли в игру!
      Возвращайтесь скорее! Буду ждать с нетерпением!
      P.S. Вы хорошо держались :)""")