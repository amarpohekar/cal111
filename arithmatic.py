'''
@file : arithematic.py
@brief  :This file is contain arithmatic operation.
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Modulus
 
'''


import math

'''
@function : add(x,b)
@brief    : It is used to ad two number
@param  : a - 1st param
          b - 2nd param
@retrun : addition of two number

'''
def add(x, y):
    c = x+y
    print("Addition ->",c)
    return 0

'''
@function : substract(x,y)
@brief    : It is used to subtrct two number
@param  : a - 1st param
          b - 2nd param
@retrun : subtraction of two number

'''
def sub(x, y):
    c = x-y
    print("subtraction-> ",c)
    return 0

'''
@function : Multiply(x,y)
@brief    : It is used to multiply two number
@param    : a - 1st param
            b - 2nd param
@return   : multiplication of two number

'''
def multiply(x, y):
    c = x * y
    print("multiplication-> ",c)
    return 0


'''
@function : Divide(x,y)
@brief    : It is used to divide number by other number
@param    : a - 1st param
            b - 2nd param
@return   : division of number by other number
'''
def divide(x, y):
    c = (x / y)
    print("division -> ",c)
    return 0

'''
@function  : modulus(x,y)
@brief     : It is used find modulus number by other number
@param    : a - 1st param
            b - 2nd param
@return   : modulus of number by other number
'''
def modulus(x, y):
    c = (x % y)
    print("modulus-> ",c)
    return 0

    

