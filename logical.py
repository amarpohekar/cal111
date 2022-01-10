'''
@file  : Logical.py
@breif : This file contain logical operation
1)AND
2)OR
3)NOT
'''

'''
@Operator : Logical AND
@brief    : True if both the operands are true.
@parame   : a = 1st param
            b = 2nd param
@Return   :  Logical operator returns True if both the value are True else it returns False.           
'''
def and_logical(x, y):
    
    if x and y:
        print("Result of and operation: True")
    else:
        print("Result of and operation: False")  
        return 0
       
'''
Operator : Logical OR
@brief   :  True if either of the operands is true.
@parame  : a = 1st param
           b = 2nd param
@return  : Logical or operator returns True if either of the value is True.              
'''
def or_logical(x, y):
    if x or y:
        print("Result of or operation: True")
    else:
        print("Result of and operation: False")
    return 0

'''
Operator  : Logical NOT
@brief    : True if both value false is false 
@parame   : a = 1st param
            b = 2nd param
@return   : If the boolean value is True it returns False and vice-versa.
'''        
def not_logical(x, y):
    if not x:
        print("result of not opertion: True")
    if not y:
         print("result of not opertion: True")
    else:
         print("result of not opertion: False")    
         return 0         
