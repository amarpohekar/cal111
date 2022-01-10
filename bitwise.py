'''
@file  : bitwise.py
@brief : This file contain bitwise operation
1) AND
2) OR
3) NOT
4) XOR
5) BITWISE RIGHT SHIFT
6) BITWISE LEFT SHIFT


  
'''

'''
@function : AND
@brief    : Returns 1 if both the bits are 1 else 0.
@param    : a - 1st param
            b - 2nd param
            
'''
def and_bitwise(x,y):
    print("X & Y= ",x & y) 
    return 0     
         
'''
@function : OR
@brief    : Returns 1 if either of the bit is 1 else 0.
@param    : a - 1st param
            b - 2nd param
            
'''

def or_bitwise(x, y):
    print("x | y= ",x | y)
    return 0


'''
@function : NOT
@brief    : Returns 1 if either of the bit is 1 else 0.
@param    : a - 1st param
        
'''

def not_bitwise(x):
    print("~x= ",~x)
    return 0

'''
@function : XOR
@brief    : Returns 1 if one of the bits is 1 
            and the other is 0 else returns false.
@param    : a - 1st param
            b - 2nd param
            
'''
def xor_bitwise(x, y):
    print("x ^ y= ",x ^ y)
    return 0

'''
@function : Bitwise right shift
@brief    : Shifts the bits of the number to the right 
            and fills 0 on voids left( fills 1 in the case of a negative number) 
            as a result.
@param    : a = 1st param

'''
def rightshift_bitwise(x):
    print("x >> 1 = ", x >> 1)
    return 0

'''
@function : bitwise left shift
@brief    : Shifts the bits of the number to the left and fills 0 on voids right as a result. 
            Similar effect as of multiplying the number with some power of two.
@param    : a = 1st param

'''
def leftshift_bitwise(x):
    print("x << 1 =", x << 1)
    return 0