import random
import matplotlib.pyplot as plt

def podgotovka(AllDigits, pomehi):
    for i in range(0, 10):
        for j in range(0, 50):
            NewElem = AllDigits[i]
            NewElem = list(NewElem)
            BasicList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            RandomNumbers = random.sample(BasicList, pomehi)
            for k in range(0, pomehi):
                NewElem[RandomNumbers[k]] ^= 1
            Rezultat.append(NewElem)
            print(i, NewElem)


def Izuchenie(W1, R1, Rezultat1, StepsCounter1, ErrorsArray1):
    ErrorsCounter = 0
    for i in range(0, 500):
        summ = 0
        for j in range(0, 9):
            summ += W1[j] * Rezultat1[i][j]
        if summ > R1 and Rezultat1[i] not in ThreeArray:
            ErrorsCounter += 1
            for k in range(0, 9):
                if Rezultat[i][k] == 1:
                    W1[k] -= 1
        elif summ <= R1 and Rezultat[i] in ThreeArray:
            ErrorsCounter += 1
            for q in range(0, 9):
                if Rezultat[i][q] == 1:
                    W1[q] += 1
    ErrorsArray1.append(ErrorsCounter)
    print(StepsCounter1)
    print(ErrorsArray1)
    if StepsCounter1 >= 1:
        if ErrorsArray1[StepsCounter1 - 1] - ErrorsArray1[StepsCounter1] == 1 or ErrorsArray1[StepsCounter1 - 1] - \
                ErrorsArray1[StepsCounter1] == -1:
            print('Исходный вектор', Wclassic)
            print('Вероятность ошибки: ', ErrorsArray1[StepsCounter1] / 500)
            print('Результат', W1)
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            y1 = Wclassic
            y2 = W1
            YSumm = y1 + y2
            Ymax = max(YSumm)
            Ymin = min(YSumm)
            plt.yticks([i for i in range(Ymin, Ymax + 1)])
            plt.xticks([i for i in range(0, 16)])
            plt.plot(x, y1, 'o-', label='Исходный вектор')
            plt.plot(x, y2, 'k', marker='o', label='Полученный результат')
            plt.legend()
            plt.show()

        elif ErrorsCounter == 0:
            print('Завершено. 0 ошибок')
            print('Исходный вектор', Wclassic)
            print('Вероятность ошибки: ', ErrorsArray1[StepsCounter1] / 500)
            print('Результат', W1)
            x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            y1 = Wclassic
            y2 = W1
            YSumm = y1 + y2
            Ymax = max(YSumm)
            Ymin = min(YSumm)
            plt.yticks([i for i in range(Ymin, Ymax + 1)])
            plt.xticks([i for i in range(0, 16)])
            plt.plot(x, y1, 'o-', label='Исходный вектор')
            plt.plot(x, y2, 'k', marker='o', label='Полученный результат')
            plt.legend()
            plt.show()
        else:
            StepsCounter1 += 1
            return Izuchenie(W1, R1, Rezultat1, StepsCounter1, ErrorsArray1)

    else:
        StepsCounter1 += 1
        return Izuchenie(W1, R1, Rezultat1, StepsCounter1, ErrorsArray1)


if __name__ == '__main__':
    Digit0 = (1, 1, 1, 0, 0, 1, 0, 1, 1)
    Digit1 = (0, 0, 1, 1, 0, 0, 0, 1, 0)
    Digit2 = (0, 1, 1, 0, 0, 0, 1, 0, 1)
    Digit3 = (0, 1, 0, 1, 1, 0, 1, 0, 0)
    Digit4 = (1, 0, 1, 0, 1, 0, 0, 1, 0)
    Digit5 = (1, 1, 0, 0, 1, 0, 0, 1, 1)
    Digit6 = (0, 0, 0, 1, 1, 1, 0, 1, 1)
    Digit7 = (0, 1, 0, 1, 0, 1, 0, 0, 0)
    Digit8 = (1, 1, 1, 0, 1, 1, 0, 1, 1)
    Digit9 = (1, 1, 1, 0, 1, 0, 1, 0, 0)

    AllDigits = (Digit0, Digit1, Digit2, Digit3, Digit4, Digit5, Digit6, Digit7, Digit8, Digit9)  # DOUBLE ARRAY

    Rezultat = []

    R = 25
    W = [1, 5, 4, 7, 6, 3, 8, 9, 3]
    Wclassic = [1, 5, 4, 7, 6, 3, 8, 9, 3]

    pomeh = 2 #pomehi=1,2,3,8,9

    podgotovka(AllDigits, pomeh)

    ThreeArray = []
    for _ in range(0, 50):
        ThreeArray.append(Rezultat[_ + 150])

    random.shuffle(Rezultat)
    StepsCounter = 0
    ErrorsArray = []

    Izuchenie(W, R, Rezultat, StepsCounter, ErrorsArray)
