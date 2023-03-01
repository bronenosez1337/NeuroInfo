num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
# Инициализация весов сети
weights = []
for i in range(15):
    weights.append(0)
# Порог функции активации
limit = 25

# Является ли данное число 4
def proceed(number):
    # Рассчёт взвешенной суммы
    net = 0
    for i in range(15):
        net += int(number[i])*weights[i]
    # Превышен ли порог? (Да - сеть думает, что это 4. Нет - сеть думает, что это другая цифра)
    return net >= limit

# Уменьшение значений весов
def decrease(number):
    for i in range(15):
        if int(number[i]) == 1:
            # Уменьшаем связанный с ним вес на единицу
            weights[i] -= 1
    print("Уменьшение весов цифры " + str(option) + " результат: " + str(weights))

# Увеличение значений весов
def increase(number):
    for i in range(15):
        if int(number[i]) == 1:
            # Увеличиваем связанный с ним вес на единицу
            weights[i] += 1
    print("Увеличение весов цифры " + str(option) + " результат: " + str(weights))
# Тренировка
train = [2,3,1,4,6,5,8,7,9,0,
         1,2,3,4,5,6,7,8,9,0,
         9,0,8,7,5,6,4,1,3,2,
         0,9,8,7,6,5,4,3,2,1,
         1,2,3,4,5,6,7,8,9,0,
         0,9,8,7,6,5,4,3,2,1,
         5,4,3,2,1,6,7,8,9,0,
         1,2,3,4,5,6,7,8,9,0,
         9,0,8,7,6,5,4,3,2,1,
         5,4,3,2,1,6,7,8,9,0]

for i in train:
    option = i
    # Преступление и наказание
    if option != 4:
        if proceed(nums[option]):
            decrease(nums[option])
    # Если получилось число 4
    else:
        # Если выдало отрицательное, то показываем, что эта цифра - то, что нам нужно
        if not proceed(num4):
            increase(num4)

# Вывод значений весов
print(weights)
# Обучающая выборка
print("0 это 4? ", proceed(num0))
print("1 это 4? ", proceed(num1))
print("2 это 4? ", proceed(num2))
print("3 это 4? ", proceed(num3))
print("4 это 4? ", proceed(num4))
print("5 это 4? ", proceed(num5))
print("6 это 4? ", proceed(num6))
print("7 это 4? ", proceed(num7))
print("8 это 4? ", proceed(num8))
print("9 это 4? ", proceed(num9), '\n')
# Тестовой выборка
print("Узнал 4? ", proceed(num4))
