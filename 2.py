import random

num0=   [True,True,True,
        True,False,True,
        True,False,True,
        True,False,True,
        True,True,True]      
num1=   [False,False,True,
        False,False,True,
        False,False,True,
        False,False,True,
        False,False,True]
num2=   [True,True,True,
        False,False,True,
        True,True,True,
        True,False,False,
        True,True,True]        
num3=   [True,True,True,
        False,False,True,
        True,True,True,
        False,False,True,
        True,True,True]        
num4=   [True,False,True,
        True,False,True,
        True,True,True,
        False,False,True,
        False,False,True]        
num5=   [True,True,True,
        True,False,False,
        True,True,True,
        False,False,True,
        True,True,True]        
num6=   [True,True,True,
        True,False,False,
        True,True,True,
        True,False,True,
        True,True,True]        
num7=   [True,True,True,
        False,False,True,
        False,False,True,
        False,False,True,
        False,False,True]        
num8=   [True,True,True,
        True,False,True,
        True,True,True,
        True,False,True,
        True,True,True]        
num9=   [True,True,True,
        True,False,True,
        True,True,True,
        False,False,True,
        True,True,True]        
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

Samples = []
R = 25

Wstart = [3, 8, 4, -4, 0, 5, 3, 4, 7, -5, 0, 3, 2, 3, 1]
W = Wstart
Noises = 1

def Interference(nums1, Noises1):  # 1,2,3,8,9
    for i in range(0, 10):
        for j in range(0, 50):
            New = nums1[i]
            New = list(New)
            BasicList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            Randoms = random.sample(BasicList, Noises1)

            for k in range(0, Noises1):
                New[Randoms[k]] = not New[Randoms[k]] # Инвертирование bool

            Samples.append(New)             #Создание выборки 
            # print(i, New)

def Training(W1, R1, Samples1, StepsCounter1, ErrorsArray1):
    ErrorsCounter = 0
    for i in range(0, 500):
        sum = 0
        for j in range(0, 15):                     # сложение весов, где true
            if Samples1[i][j]: sum += W1[j]

        if sum > R1 and Samples1[i] not in FivesArr:     # Если сумма превысила порог и это не 5
            ErrorsCounter += 1                           # Считаем ошибку
            for k in range(0, 15):
                if Samples1[i][k] == 1:                      
                    W1[k] -= 1                           # и уменьшаем омеги
        elif sum <= R1 and Samples1[i] in FivesArr:      # иначе если сумма меньше порога и это 5
            ErrorsCounter += 1                           # Считаем ошибку
            for q in range(0, 15):
                if Samples1[i][q] == 1:                 # и увеличиваем омеги
                    W1[q] += 1
        else: pass                      # Если всё подходит, ничего не меняем
    
    ErrorsArray1.append(ErrorsCounter)               # Запись в массив ошибок 
    print("Итерация {0}".format(StepsCounter1))      #Вывод итераций и массива ошибок
    print("Ошибки: {0}".format(ErrorsArray1))

    if StepsCounter1 >= 1:

        if ErrorsArray1[StepsCounter1 - 1] - ErrorsArray1[StepsCounter1] == 0 or ErrorsArray1[StepsCounter1 - 1] - ErrorsArray1[StepsCounter1] == 1 or ErrorsArray1[StepsCounter1 - 1] - ErrorsArray1[StepsCounter1] == -1 or ErrorsCounter == 0:
            '''Если в предыдущей итерации было на 1 ошибку больше или на 1 ошибку меньше, или ошибок нет'''    
            print('\nИзначальные веса: {0}'.format(Wstart))
            print('Вероятность ошибки: {0}'.format(ErrorsArray1[StepsCounter1] / 500))
            print('Итоговые веса: {0}'.format(W1))

        else:
            '''Иначе повторить обучение, увеличив счётчик итераций'''
            StepsCounter1 += 1
            return Training(W1, R1, Samples1, StepsCounter1, ErrorsArray1)

    else:
        '''принудительно повторить обучение второй раз'''
        StepsCounter1 += 1
        return Training(W1, R1,Samples1 , StepsCounter1, ErrorsArray1)

Interference(nums, Noises)

FivesArr = []
for _ in range(0, 50):
    FivesArr.append(Samples[_ + 250])    # Записываем массив возможных пятёрок

random.shuffle(Samples)                  # Перемешиваем выборку
StepsCounter = 0
ErrorsArray = []
#Вызов функции тренировки
Training(W, R, Samples, StepsCounter, ErrorsArray)
