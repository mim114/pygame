from random import randint

lowDiapazon  = 10    # нижняя граница чисел
highDiapazon = 100   # верхняя граница чисел
sign         = 0     # знак операции
playGame     = True  # главный цмкл
count        = 0     # количество решённых примеров
right        = 0     # количество правильных решённых примеров
score        = 0     # очки

print("""Компьютер составляет пример. Введите ответ.
      Для завершения работы введите STOP.""")
print('*' * 40)

while playGame:
    print(f"Ваши очки: {score}")
    print(f"Обработанно задачи: {count}")
    print(f"Правельных ответов: {right}")
    print('-' * 20)

    # 0 - +
    # 1 - -
    # 2 - *
    # 3 - /
    sign = randint(0, 3)

    if sign == 0:
        z = randint(lowDiapazon, highDiapazon)
        x = randint(lowDiapazon, z)
        y = z - x

        if randint(0, 1) == 0:
            print(f"{x} + {y} = ?")
        else:
            print(f"{y} + {x} = ?")
    elif sign == 1:
        x = randint(lowDiapazon, highDiapazon)
        y = randint(0, x - lowDiapazon)
        z = x - y
        print(f"{x} - {y} = ?")
    elif sign == 2:
        x = randint(1, (highDiapazon - lowDiapazon) // randint(1, highDiapazon // 10) + 1)
        y = randint(lowDiapazon, highDiapazon) // x
        z = x * y
        print(f"{x} * {y} = ?")
    elif sign == 3:
        x = randint(1, (highDiapazon - lowDiapazon) // randint(1, highDiapazon // 10) + 1)
        y = randint(lowDiapazon, highDiapazon) // x

        if y == 0:
            y = 1
        
        x = x * y
        z = int(x / y)
        print(f"{x} / {y} = ?")

    user = ""

    while (not user.isdigit()
                and user.upper() != "STOP"
                and user.upper() != "S"
                and user.upper() != "Ы"
                and user.upper() != "ЫЕЩЗ"):
            
                user = input("Введите ответ: ")

                if (user.upper() == "HELP"
                    or user == '?'
                    or user == ','
                    or user.upper() == "РУДЗ"):

                    if z > 9:
                        print(f"Последняя цифра ответа: {z % 10}")
                    else:
                        print(f"Ответ состоит из одной цифры, подсказка невозможна.")
                    
                    score -= 10
                elif (user.upper() == "STOP"
                    or user.upper() == "S"
                    or user.upper() == "Ы"
                    or user.upper() == "ЫЕЩЗ"):
                    playGame = False
                else:
                    count += 1

                    if user.isdigit():
                        if int(user) == z:
                            print("\nПравильно!\n")
                            right += 1
                            score += 10
                        else:
                            print(f"\nНеправильно... Верный ответ {z}\n")
                            print(f"Вы можете ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (-10 очков)\n")
                            score -= 10
                    else:
                        continue

print('*' * 40)
print("СТАТИСТИКА ИГРЫ:")
print(f"Всего примеров: {count}")
print(f"Правильных ответов: {right}")
print(f"Неправильных ответов: {count - right}")

if count > 0:
    print(f"Процент верных ответов: {int(right / count * 100)}%")
else:
    print(f"Процент верных ответов: 0%")

print("Возвращайтесь!")