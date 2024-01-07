import random
import time

valuta = '$'
money = 0
startMoney = 0
playGame = True
defaultMoney = 10000

# функция изменения цвета
def color(c):
    return f"\033[0;{c}m"

# функция ввода целого числа
def getIntInput(minimum, maximum, message):
    print(color(37))
    ret = -1

    while ret < minimum or ret > maximum:
        st = input(message)

        if st.isdigit():
            ret = int(st)
        else:
            print("Введите целое число!")

    return ret

# функция ввода значения
def getInput(digit, message):
    print(color(37))
    ret = ""

    while ret == "" or not ret in digit:
        ret = input(message)

    return ret

# процесс вывода на экран цветного, обрамлённого звёздочками текста
def colorLine(c, s):
    for i in range(35):
        print()

    print(color(c))
    print('*' * (len(s) * 2))
    print(' ' + s)
    print('*' * (len(s) * 2))

# процес сообщающий о победе
def pobeda(result):
    print(color(33))
    print(f"    Победа за вами! Выигрыш составил: {valuta}{result}")
    print(f"    У вас на счету: {money}")

# процес сообщающий о проигрыше
def proigr(result):
    print(color(31))
    print(f"   К сожалению, Вы проиграли: {valuta}{result}")
    print(f"   У вас на счету: {money}")

# фунция чтения из файла оставшейся суммы
def loadMoney():
    try:
        f = open("money.txt", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Не найден файл с суммой! Задано значение {valuta}{defaultMoney}") 
        m = defaultMoney
    return m

# функция записи в файл с суммой
def saveMoney(m):
    try:
        f = open("money.txt", "w")
        f.write(str(m))
        f.close()
    except FileNotFoundError:
        print("Ошибка создания файла, Казино закрывается!")
        quit()

# анимация рулетки и возврат числа
def getRoulette(visible):
    tickTime = random.randint(100, 200) / 10000
    # пауза в сикундах
    mainTime = 0
    number = random.randint(0, 38)
    # на сколько увеличить tickTime
    increaseTickTime = random.randint(100, 110) / 100
    col = 30

    while mainTime < 0.7:
        col += 1
        
        if col > 37:
            col =31

        # увеличение времени паузы
        mainTime += tickTime
        tickTime *= increaseTickTime
        # увеличение номера и вывод на экран
        print(color(col))
        number += 1

        if number > 38:
            number = 0
            print()
        
        # обработка "00" "000"
        printNumber = number

        if number == 37:
            printNumber = "00"
        elif number == 38:
            printNumber = "000"

        # вывод на экран
        print(" Число >", printNumber, '*' * number, ' ' * (79 - number * 2),
              '*' * number)
        # пауза в зависемости от visible
        if visible:
            time.sleep(mainTime)
    
    return number

# рулетка
def roulette():
    global money
    playGame = True

    while playGame and money > 0:
        # вывод меню
        colorLine(33, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
        print(color(34))
        print(f"\n У вас на считу {valuta}{money}\n")
        print(color(31))
        print(" Ставлю на ...")
        print("    1. Чётное   (выигрыш  1:1)")
        print("    2. Нечётное (выигрыш  1:1)")
        print("    3. Дюжина   (выигрыш  3:1)")
        print("    4. Число    (выигрыш 36:1)")
        print("    0. Возврат в предыдущее меню")
        # ввод значения, выбор меню
        x = getInput("01234", "    Ваш выбор? ")
        playRoulette = True

        if x == '3':
            print(color(32))
            print("    Выберите числа:...")
            print("    1. От 1 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Назад")
            duzhina = getInput("0123", "    Ваш выбор? ")

            if duzhina == '1':
                textDuzhina = "от 1 до 12"
            elif duzhina == '2':
                textDuzhina = "от 13 до 24"
            elif duzhina == '3':
                textDuzhina = "от 25 до 36"
            elif duzhina == '0':
                playRoulette = False
        elif x == '4':
            chislo = getIntInput(0, 36, "    На какое число ставите? (0..36): ")
        
        print(color(37))

        if x == '0':
            return 0
        
        if playRoulette:
            stavka = getIntInput(0, money, f"    Сколько ставите? (не болеее {money}): ")

            if stavka == 0:
                return 0
            number = getRoulette(True)
            print(color(31))

            if number < 37:
                print(f"    Выпало число {number}! " + '*' * number)
            else:
                if number == 37:
                    printNumber = "00"
                elif number == 38:
                    printNumber = "000"
                print(f"    Выпало число {printNumber}! ")

            # проверяем ставки и результат
            if x == '1':
                print("    Вы ставили на ЧЁТНОЕ!")
                if number < 37 and number % 2 == 0:
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)
            elif x == '2':
                print("    Вы ставили на НЕЧЁТНОЕ!")
                if number < 377 and number % 2 != 0:
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)
            elif x == '3':
                print(f"    Ставка сделана на диапазон чисел {textDuzhina}.")
                winDuzhina = ""
                if number > 0 and number < 13:
                    winDuzhina = '1'
                elif number > 12 and number < 25:
                    winDuzhina = '2'
                elif number > 24 and number < 37:
                    winDuzhina = '3'
                
                if duzhina == winDuzhina:
                    money += stavka * 2
                    pobeda(stavka * 3)
                else:
                    money -= stavka
                    proigr(stavka)
            elif x == '4':
                print(f"    Ставка сделана на число {chislo}")
                if number == chislo:
                    money += stavka * 35
                    pobeda(stavka * 36)
                else:
                    money -= stavka
                    proigr(stavka)
        
        print()
        input(" Нажмите Enter для продолжения...")

# анемирование костей
def getDice():
    count = random.randint(1, 7)
    sleep = 0

    while count > 0:
        print(color(count + 30))
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(' ' * 10, "----- -----")
        print(' ' * 10, f"| {x} | | {y} |")
        print(' ' * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1

    return x + y

# кости
def dice():
    global money
    playGame = True

    while playGame:
        print()
        colorLine(33, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        print(color(34))
        print(f"\n У вас на считу {valuta}{money}\n")
        print(color(37)) 
        stavka =getIntInput(0, money, f"    Сделайте ставку в пределах {valuta}{money}(0-выход): ")

        if stavka == 0:
            return 0
        
        playRound = True
        control = stavka
        oldResult = getDice()
        firstPlay = True

        while playRound and stavka > 0 and money > 0:
            if stavka > money:
                stavka = money

            print(color(31))
            print(f"\n    Поставленно в БАНК: {valuta}{stavka}")
            print(color(32))
            print(f"\n     Текущая сумма чисел на костях: {oldResult}")
            print(color(31))
            print("\n    Сумма чисел на гранях будет БОЛЬШЕ, МЕНЬШЕ или РАВНА предудущей?")
            print(color(37))
            x = getInput("01234", "    Введи 1-больше 2-меньше 3-равно 0-выход: ")

            if x != '0':
                firstPlay = False
                if stavka > money:
                    stavka = money

                money -= stavka
                diceResult = getDice()
                win = False

                if oldResult > diceResult:
                    if x == '2':
                        win = True
                elif oldResult < diceResult:
                    if x == '1':
                        win = True

                if not x == '3':
                    if win:
                        money += stavka + stavka // 5
                        pobeda(stavka // 5)
                        stavka += stavka // 5
                    else:
                        stavka = control
                        proigr(stavka)
                elif x == '3':
                    if oldResult == diceResult:
                        money += stavka * 3
                        pobeda(stavka * 2)
                        stavka *= 3
                    else:
                        stavka = control
                        proigr(stavka)

                oldResult = diceResult

            else:
                # если выход на первой ставке
                if firstPlay:
                    money -= stavka
                playRound = False

def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0

    if digit == v1: ret += 1
    if digit == v2: ret += 1
    if digit == v3: ret += 1
    if digit == v4: ret += 1
    if digit == v5: ret += 1
    return ret

# анемирывание однорукого бандита
def getOHBRes(stavka):
    res = stavka
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True
    col = 31

    while getD1 or getD2 or getD3 or getD4 or getD5:
        if getD1: d1 += 1
        if getD2: d2 -= 1
        if getD3: d3 += 1
        if getD4: d4 -= 1
        if getD5: d5 += 1
        if d1 > 9: d1 = 0
        if d2 < 0: d2 = 9
        if d3 > 9: d3 = 0
        if d4 < 0: d4 = 9
        if d5 > 9: d5 = 0
        if random.randint(0, 20) == 1: getD1 = False
        if random.randint(0, 20) == 1: getD2 = False
        if random.randint(0, 20) == 1: getD3 = False
        if random.randint(0, 20) == 1: getD4 = False
        if random.randint(0, 20) == 1: getD5 = False

        time.sleep(0.1)
        print(color(col))
        col += 1

        if col > 38: col = 31

        print("    " + '%' * 10)
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

    if maxCount < getMaxCount(d2, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d3, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d4, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if maxCount < getMaxCount(d5, d1, d2, d3, d4, d5):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)

    print(color(34))

    if maxCount == 2:
        print(f" Совпадение двух чисел! Ваш выигрыш в размере ставки {res}")
    elif maxCount == 3:
        res *= 2
        print(f" Совпадение трёх чисел! Ваш выигрыш 2:1: {res}")
    elif maxCount == 4:
        res *= 5
        print(f" Совпадение ЧЕТЫРЁХ чисел! Ваш выигрыш 5:1: {res}")
    elif maxCount == 5:
        res *= 10
        print(f" БИНГО!!! Совпадение ВСЕХ чисел! Ваш выигрыш 10:1: {res}")
    else:
        proigr(res)
        res = 0

    print(color(31))
    input(" Нажмите Enter для продолжения...")
    return res

#однорукий бандит
def oneHandBandit():
    global money
    playGame = True

    while playGame:
        colorLine(33, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
        print(color(34))
        print(f"\n У вас на считу {valuta}{money}\n")
        print(color(35))
        print(" Правила игры:")
        print("    1. При совпадении 2-х  чисел ставка не списывается")
        print("    2. При совпадении 3-х  чисел выигрыш  2:1")
        print("    3. При совпадении 4-х  чисел выигрыш  5:1")
        print("    4. При совпадении 5-ти чисел выигрыш 10:1")
        print("    0. Ставка 0 для завершения игры\n")
        stavka = getIntInput(0, money, f"    Введите ставку от 0 до {money}: ")

        if stavka == 0:
            return 0
        
        money -= stavka
        money += getOHBRes(stavka)

        if money <= 0:
            playGame = False

def main():
    global money, playGame
    money = loadMoney()
    startMoney = money

    while (playGame and money) > 0:
        colorLine(33, "Приветствую вас в нашем казино!")
        print(color(34))
        print(f"У вас на счету {valuta}{money}")
        print(color(36))
        print(" Вы можете сыграть в:")
        print("    1. Рулетку")
        print("    2. Кости")
        print("    3. Однорукого бандита")
        print("    0. Выход. Ставка 0 в играх - выход.")
        #print(color(37))
        x = getInput("0123", "    Ваш выбор? ")

        if x == '0':
            playGame = False
        elif x == '1':
            roulette()
        elif x == '2':
            dice()
        elif x == '3':
            oneHandBandit()

    colorLine(12, "Жаль, что вы покидаете нас! Возвращайтесь скорее")
    print(color(33))

    if money <= 0:
        print(" Упс, вы остались без денег. Возьмите кредит и возвращайтесь!")
    
    print(color(32))

    if money > startMoney:
        print("Ну что ж, поздравляем с прибылью!")
        print(f"На начало игры у вас было  {valuta}{startMoney}")
        print(f"Сейчас уже {valuta}{money}! Играйте ещё и приумножайте!")
    else:
        print(f"К сожалению, вы проиграли  {valuta}{startMoney - money}")
        print("В следующий раз всё обязательно получится!")

    saveMoney(money)
    color(37)
    quit()

main()