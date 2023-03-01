import numpy as np
from random import randint

def schet(number):
    summary = 0
    for y in range(len(number)):
        if number[y]: summary+=w[y]
    print ('F = ', summary)
    print ('Is a 5?', end='\t')    
    if summary>=Q: print('yes\n')
    else: print('no\n')
    return summary
# def increase():
#     if schet() ==  :
        
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
num0= np.array([True,True,True,
                True,False,True,
                True,False,True,
                True,False,True,
                True,True,True],bool)

w= np.array([2, 2, 2, 3, 0, -10, 2, 2, 2, -8, 0, 3, 2, 2, 2])
Q = 25
print ('1')
sum1 = schet(num1)
print ('2')
sum2 = schet(num2)
print ('3')
sum3 = schet(num3)
print ('4')
sum4 = schet(num4)
print ('5')
sum5 = schet(num5)
print ('6')
sum6 = schet(num6)
print ('7')
sum7 = schet(num7)
print ('8')
sum8 = schet(num8)
print ('9')
sum9 = schet(num9)
print ('0')
sum0 = schet(num0)






i=1               
for x in range(len(num3)):
    if num0[x]: print ('X',end='   ')
    else: print('.',end='   ')
    if (i%3==0): print ('\n')
    i+=1