import numpy as np
from random import randint
index=30
w = []
for i in range(15):
    w.append(0)
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
for i in range(200):
    training.append(randint(0,9))
print ("Выбока из {0} чисел для обучения сети = {1}".format(len(training),training))

def schet(number):
    summary = 0
    for y in range(len(number)):
        if number[y]: summary+=w[y]
        #Возвращает значение если сумма омег будет больше индекса
    return summary >= index

def reward(number):
    for z in range(len(number)):
        if number[z]:
            w[z] +=1
    print("Омеги были увеличены и теперь = {0}".format(w))
def penalty(number):
    for z in range(len(number)):
        if number[z]:
            w[z] -=1
    
    print("Омеги были уменьшены и теперь = {0}".format(w))

num0= np.array([True,True,True,
                True,False,True,
                True,False,True,
                True,False,True,
                True,True,True],bool)         
num1= np.array([False,False,True,
                False,True,True,
                True,False,True,
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




    

for i in training:
    if i != 5:
    #   если это не 5, и сумма омег больше индекса, то уменьшить нужные омеги на 1
        if schet(nums[i]):
            penalty(nums[i])
    else:
    #  если это 5, и сумма омег больше индекса, то увеличить нужные омеги на 1
        if not schet((num5)):
            reward(num5)


if schet(num0): print ("0 is a 5?\t Yes")
else: print("0 is a 5?\t No")
if schet(num1): print ("1 is a 5?\t Yes")
else: print("1 is a 5?\t No")
if schet(num2): print ("2 is a 5?\t Yes")
else: print("2 is a 5?\t No")
if schet(num3): print ("3 is a 5?\t Yes")
else: print("3 is a 5?\t No")
if schet(num4): print ("4 is a 5?\t Yes")
else: print("4 is a 5?\t No")
if schet(num5): print ("5 is a 5?\t Yes")
else: print("5 is a 5?\t No")
if schet(num6): print ("6 is a 5?\t Yes")
else: print("6 is a 5?\t No")
if schet(num7): print ("7 is a 5?\t Yes")
else: print("7 is a 5?\t No")
if schet(num8): print ("8 is a 5?\t Yes")
else: print("8 is a 5?\t No")
if schet(num9): print ("9 is a 5?\t Yes")
else: print("9 is a 5?\t No")
