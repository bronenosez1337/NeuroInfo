import numpy as np
import random 
index=35
w = [4,1,3,2,6,8,4,2,0,4,1,7,0,5,3]
errors = 0
# for i in range(15):
#     w.append(0)
# фиксированная выборка
# training = [3, 0, 5, 1, 3, 4, 1, 3, 4, 6,
#              9, 3, 1, 4, 1, 2, 4, 7, 0, 9,
#              9, 5, 8, 7, 4, 2, 5, 7, 2, 1, 
#              5, 7, 4, 0, 4, 3, 0, 2, 6, 8, 
#              1, 5, 7, 5, 8, 9, 5, 3, 2, 9, 
#              2, 2, 3, 8, 1, 9, 9, 8, 7, 6, 
#              5, 0, 6, 6, 9, 9, 3, 4, 5, 1, 
#              7, 8, 5, 5, 9, 2, 4, 3, 4, 9, 
#              0, 8, 5, 3, 5, 3, 4, 6, 8, 2, 
#              4, 5, 3, 2, 9, 3, 5, 6, 3, 2]
training = []
# Случайная выборка
for i in range(300):
    training.append(random.randint(0,9))
print ("Выбока из {0} чисел для обучения сети = {1}".format(len(training),training))

def podgotovka(AllDigits, pomehi):
    for i in range(0, 10):
        
        NewElem = AllDigits[i]
        NewElem = list(NewElem)
        BasicList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        RandomNumbers = random.sample(BasicList, pomehi)
        for k in range(0, pomehi):
            NewElem[RandomNumbers[k]] = not NewElem[RandomNumbers[k]]
        Result.append(NewElem)
        print(i, NewElem)

def schet(number):
    summary = 0
    for y in range(len(number)):
        if number[y]: 
            summary+=w[y]
        #Возвращает значение если сумма омег будет больше индекса
    return summary >= index

def reward(number):
    for z in range(len(number)):
        if number[z]:
            w[z] +=1
    global errors
    errors+=1
    print("Омеги были увеличены и теперь = {0}".format(w))

def penalty(number):
    for z in range(len(number)):
        if number[z]:
            w[z] -=1
    global errors        
    errors+=1        
    print("Омеги были уменьшены и теперь = {0}".format(w))

num0= np.array([True,True,True,
                True,False,True,
                True,False,True,
                True,False,True,
                True,True,True],bool)         
num1= np.array([False,False,True,
                False,False,True,
                False,False,True,
                False,False,True,
                False,False,True],bool)
num2= np.array([True,True,True,
                False,False,True,
                True,True,True,
                True,False,False,
                True,True,True],bool)
num3= np.array([True,True,True,
                False,False,True,
                True,True,True,
                False,False,True,
                True,True,True],bool)
num4= np.array([True,False,True,
                True,False,True,
                True,True,True,
                False,False,True,
                False,False,True],bool)
num5= np.array([True,True,True,
                True,False,False,
                True,True,True,
                False,False,True,
                True,True,True],bool) 
num6= np.array([True,True,True,
                True,False,False,
                True,True,True,
                True,False,True,
                True,True,True],bool) 
num7= np.array([True,True,True,
                False,False,True,
                False,False,True,
                False,False,True,
                False,False,True],bool)
num8= np.array([True,True,True,
                True,False,True,
                True,True,True,
                True,False,True,
                True,True,True],bool) 
num9= np.array([True,True,True,
                True,False,True,
                True,True,True,
                False,False,True,
                True,True,True],bool)
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]
# w= np.array([4,7,4,9,1,-2,3,6,8,-2,12,11,15,1,14])

pomehi = 15
Result=[]
podgotovka(nums,pomehi)


for i in training:
    if i != 5:
    #   если это не 5, и сумма омег больше индекса, то уменьшить нужные омеги на 1
        if schet(Result[i]):
            penalty(Result[i])
    else:
    #  если это 5, и сумма омег больше индекса, то увеличить нужные омеги на 1
        if not schet((Result[5])):
            reward(Result[5])


if schet(Result[0]): print ("0 is a 5?\t Yes")
else: print("0 is a 5?\t No")
if schet(Result[1]): print ("1 is a 5?\t Yes")
else: print("1 is a 5?\t No")
if schet(Result[2]): print ("2 is a 5?\t Yes")
else: print("2 is a 5?\t No")
if schet(Result[3]): print ("3 is a 5?\t Yes")
else: print("3 is a 5?\t No")
if schet(Result[4]): print ("4 is a 5?\t Yes")
else: print("4 is a 5?\t No")
if schet(Result[5]): print ("5 is a 5?\t Yes")
else: print("5 is a 5?\t No")
if schet(Result[6]): print ("6 is a 5?\t Yes")
else: print("6 is a 5?\t No")
if schet(Result[7]): print ("7 is a 5?\t Yes")
else: print("7 is a 5?\t No")
if schet(Result[8]): print ("8 is a 5?\t Yes")
else: print("8 is a 5?\t No")
if schet(Result[9]): print ("9 is a 5?\t Yes")
else: print("9 is a 5?\t No")
print ("Кол-во ошибок: {0}".format(errors))

